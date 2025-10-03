-- 20250116112200_fix_job_locking_for_text_ids.sql

-- 1) Drop the old function definitions so we can recreate them with text parameters
DROP FUNCTION IF EXISTS acquire_job(uuid, text) CASCADE;
DROP FUNCTION IF EXISTS update_job_status_if_in_progress(uuid, text, text, jsonb, text) CASCADE;

-- 2) Create the new functions, which expect a text job_id instead of uuid

CREATE OR REPLACE FUNCTION acquire_job(
    _job_id text,    -- now text, not uuid
    _worker_id text
)
RETURNS SETOF jobs
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  UPDATE jobs
     SET status = 'in_progress',
         worker_id = _worker_id
   WHERE id = _job_id
     AND status = 'pending'
  RETURNING *;
END;
$$;


CREATE OR REPLACE FUNCTION update_job_status_if_in_progress(
    _job_id text,       -- now text, not uuid
    _new_status text,
    _worker_id text,
    _job_outputs jsonb DEFAULT null,
    _job_script text DEFAULT null
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE jobs
     SET status = _new_status,
         outputs = _job_outputs,
         script = COALESCE(_job_script, script)
   WHERE id = _job_id
     AND status = 'in_progress'
     AND worker_id = _worker_id;
END;
$$;

-- 3) Grant necessary permissions so authenticated users (or whichever role) can execute
GRANT EXECUTE ON FUNCTION acquire_job(text, text) TO authenticated;
GRANT EXECUTE ON FUNCTION update_job_status_if_in_progress(text, text, text, jsonb, text) TO authenticated;
