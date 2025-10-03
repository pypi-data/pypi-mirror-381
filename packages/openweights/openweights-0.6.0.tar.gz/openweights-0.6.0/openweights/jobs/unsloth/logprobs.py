import json
import math
import os
import sys

import torch
import torch.nn.functional as F
from datasets import Dataset
from transformers import TrainerCallback
from utils import client, load_jsonl, load_model_and_tokenizer

# Helper utilities to normalize message content formats
# Allows both string content and block-formatted content


def content_to_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block["text"] if isinstance(block, dict) and "text" in block else str(block)
            for block in content
        )
    return str(content)


def ensure_block_list(content):
    if isinstance(content, list):
        # If already list of dict blocks with 'text', return as is
        if len(content) == 0 or (isinstance(content[0], dict) and "text" in content[0]):
            return content
        # If list of strings or mixed, collapse to a single text block
        joined = "".join(
            block if isinstance(block, str) else str(block) for block in content
        )
        return [{"type": "text", "text": joined}]
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    # Fallback: stringify unknown types
    return [{"type": "text", "text": str(content)}]


def apply_chat_template(tokenizer, batch):
    if "text" in batch:
        return batch
    conversations = batch["messages"]
    texts = []
    for conversation in conversations:
        text = tokenizer.apply_chat_template(
            conversation,
            add_generation_prompt=False,
            return_tensors="pt",
            tokenize=False,
        )
        if not text.strip().endswith(tokenizer.eos_token):
            text += tokenizer.eos_token
        texts.append(text)
    return texts


def batch_tokenize(tokenizer, batch):
    texts = apply_chat_template(tokenizer, batch)
    input_ids = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=8196,
        add_special_tokens=False,
        return_tensors="pt",
    )["input_ids"]
    return input_ids


def _prepare_batch(tokenizer, batch):
    """Prepare a batch of messages for the model."""
    input_ids = batch_tokenize(tokenizer, batch)
    # Create attention mask (1 for real tokens, 0 for padding)
    attention_mask = (input_ids != tokenizer.pad_token_id).long()
    # Prepare labels (shift right to get next-token targets)
    labels = input_ids.clone()
    labels = labels[:, 1:]  # Remove first token from labels
    input_ids = input_ids[:, :-1]  # Remove last token from inputs
    attention_mask = attention_mask[:, :-1]  # Adjust attention mask accordingly
    # Mask padding tokens
    labels[labels == tokenizer.pad_token_id] = -100
    return input_ids, attention_mask, labels


def get_logprobs(model, tokenizer, test_dataset, batch_size):
    total_loss = 0
    token_logp = []

    with torch.no_grad():
        # Process test dataset in batches
        for i in range(0, len(test_dataset), batch_size):
            batch = test_dataset[i : i + batch_size]

            # Prepare batch data
            input_ids, attention_mask, labels = _prepare_batch(tokenizer, batch)

            # Move tensors to model device
            input_ids = input_ids.to(model.device)
            attention_mask = attention_mask.to(model.device)
            labels = labels.to(model.device)

            # Forward pass
            outputs = model(
                input_ids=input_ids, attention_mask=attention_mask, labels=labels
            )

            # Get logits and move to CPU
            logits = outputs.logits.detach().cpu().float()
            labels_cpu = labels.cpu()

            # Calculate log probabilities
            log_probs = F.log_softmax(logits, dim=-1)

            # Create mask for valid (non-padding) tokens
            valid_tokens = labels_cpu != -100

            # Replace -100 labels with 0 (or any valid token id) for gather operation
            gather_labels = labels_cpu.clone()
            gather_labels[~valid_tokens] = 0

            # Calculate token-level log probabilities
            token_log_probs = log_probs.gather(-1, gather_labels.unsqueeze(-1)).squeeze(
                -1
            )

            # Apply the mask to zero out padding tokens
            masked_log_probs = token_log_probs * valid_tokens.float()

            # Calculate average loss for this batch
            batch_loss = -masked_log_probs.sum() / valid_tokens.sum()
            total_loss += batch_loss.item()

            for batch_idx, messages in enumerate(batch["messages"]):
                token_logp.append(
                    {
                        "messages": messages,
                        "tokens": [
                            {
                                "token": tokenizer.decode(token.item()),
                                "token_id": token.item(),
                                "logp": logp.item(),
                            }
                            for token, logp in zip(
                                labels[batch_idx], masked_log_probs[batch_idx]
                            )
                            if token != tokenizer.pad_token_id and token != -100
                        ],
                    }
                )
    return token_logp, total_loss


def convs_to_ds(convs):
    batch = {"messages": []}
    for conv in convs:
        processed_messages = []
        for message in conv["messages"]:
            processed_messages.append(
                dict(role=message["role"], content=content_to_text(message["content"]))
            )
        batch["messages"].append(processed_messages)
    return Dataset.from_dict(batch)


def get_logprobs_blockwise(model, tokenizer, convs, batch_size=4):
    """
    Get token-level log probabilities and map them back to the original conversation structure.
    Conversations are expected to be in content-block format.
    """
    ds = convs_to_ds(convs)
    token_logprobs, _ = get_logprobs(model, tokenizer, ds, batch_size)
    processed_convs = []
    for conv_idx, conv in enumerate(convs):
        processed_conv = get_logprobs_blockwise_single_conv(
            conv, token_logprobs[conv_idx], tokenizer
        )
        processed_convs.append(processed_conv)
    return processed_convs


def tokenize_block_formatted_conversation(tokenizer, conversation):
    """Tokenize a conversation formatted as a list of messages with content blocks."""
    messages_copy = [dict(**m) for m in conversation]
    # Convert content blocks to strings
    for m in messages_copy:
        m["content"] = content_to_text(m["content"])
    # Get tokens with the full message
    return tokenizer.apply_chat_template(
        messages_copy, return_tensors="pt", tokenize=True
    ).squeeze(0)


def find_common_prefix_length(tokens1, tokens2):
    """Find the length of the common prefix between two sequences of tokens."""
    prefix_length = 0
    for t1, t2 in zip(tokens1, tokens2):
        if t1 == t2:
            prefix_length += 1
        else:
            break
    return prefix_length


def find_end_of_block(tokens, block_text):
    """Find the length of the block in tokens."""
    block_length, rec = 0, ""
    for token in tokens:
        if block_text in rec:
            return block_length
        rec += token
        block_length += 1
    raise ValueError(f"Block `{block_text}` not found in tokens: {tokens}")


def get_logprobs_blockwise_single_conv(conv, token_logprobs, tokenizer):
    """Process a single conversation, mapping tokens to message blocks."""
    messages = conv["messages"]
    tokens = token_logprobs["tokens"]
    tokens_str = [t["token"] for t in tokens]

    processed_messages = []
    for original_message in messages:
        current_message = {"role": original_message["role"], "content": []}
        before_block = tokenize_block_formatted_conversation(
            tokenizer, processed_messages + [current_message]
        )
        for block in ensure_block_list(original_message["content"]):
            current_message["content"].append(block)
            with_block = tokenize_block_formatted_conversation(
                tokenizer, processed_messages + [current_message]
            )
            block_start = (
                find_common_prefix_length(before_block, with_block) - 1
            )  # -1 is because tokens are derived from labels, which are shifted by 1 from inputs
            block_length = find_end_of_block(tokens_str[block_start:], block["text"])
            block_tokens = tokens[block_start : block_start + block_length]
            rec_text = "".join([t["token"] for t in block_tokens])
            if rec_text != block["text"]:
                print("Mismatch:", rec_text, block["text"])
            if block.get("logprobs", True) is not False:
                block["logprobs"] = sum([t["logp"] for t in block_tokens])
            block["range"] = (block_start, block_start + block_length)
            before_block = with_block
        processed_messages.append(current_message)
    processed_conv = dict(**conv)
    processed_conv["messages"] = processed_messages
    return processed_conv


def main(config_job_id: str):
    os.environ["UNSLOTH_RETURN_LOGITS"] = "1"
    if os.path.exists(config_job_id):
        with open(config_job_id, "r") as f:
            config = json.load(f)
    else:
        job = client.jobs.retrieve(config_job_id)
        config = job["params"]["params"]

    # Load model and tokenizer
    model, tokenizer = load_model_and_tokenizer(config["model"])

    dataset = load_jsonl(config["dataset"])
    logprobs = get_logprobs_blockwise(model, tokenizer, dataset, config["batch_size"])
    # Write jsonl
    with open("logprobs.jsonl", "w") as f:
        for conv in logprobs:
            f.write(json.dumps(conv) + "\n")
    # Upload to client
    with open("logprobs.jsonl", "rb") as f:
        logprobs_file = client.files.create(f, purpose="logprobs")
    client.run.log({"type": "logprobs", "file": logprobs_file["id"]})


if __name__ == "__main__":
    main(sys.argv[1])
