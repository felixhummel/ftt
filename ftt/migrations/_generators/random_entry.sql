--
-- generate semi-random entries
--

CREATE OR REPLACE FUNCTION random_dt(start_dt TIMESTAMPTZ, end_dt TIMESTAMPTZ)
  RETURNS TIMESTAMPTZ
AS $$
SELECT start_dt + random() * (end_dt - start_dt);
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION insert_random_entry(dt DATE, project_id INTEGER, user_id INTEGER)
  RETURNS VOID
AS $$
DECLARE
  start_dt TIMESTAMPTZ;
  end_dt   TIMESTAMPTZ;
  comment  TEXT := 'randomly generated';
BEGIN
  -- work-day begins between 8 and 11
  start_dt := (SELECT random_dt(
      dt + '08:00' :: TIMETZ,
      dt + '11:00' :: TIMETZ
  ));
  -- and ends between 16 and 19
  end_dt := (SELECT random_dt(
      dt + '16:00' :: TIMETZ,
      dt + '19:00' :: TIMETZ
  ));
  INSERT INTO ftt_entry (
    start_dt, end_dt, comment, project_id, user_id
  ) VALUES (
    start_dt, end_dt, comment, project_id, user_id
  );
END
$$ LANGUAGE PLPGSQL;

DROP VIEW IF EXISTS test_dates;
CREATE OR REPLACE TEMPORARY VIEW test_dates AS
  SELECT
    -- some dates
    generate_series(
        '2016-06-01' :: DATE,
        '2017-03-17' :: DATE,
        '1 day'
    ) AS dt;
-- SELECT *
-- FROM dates;

CREATE OR REPLACE FUNCTION insert_random_entries()
  RETURNS VOID
AS $$
DECLARE
  entry_dt   DATE;
  project_id INTEGER;
  user_id    INTEGER;
BEGIN
  user_id := (
    SELECT id
    FROM auth_user
    WHERE username = 'admin');
  FOR entry_dt IN SELECT dt
                  FROM test_dates LOOP
    project_id := (
      SELECT id
      FROM ftt_project
      ORDER BY random()
      LIMIT 1
    );
    PERFORM insert_random_entry(entry_dt, project_id, user_id);
  END LOOP;
END
$$ LANGUAGE PLPGSQL;

DELETE
FROM ftt_entry
WHERE comment = 'randomly generated';
SELECT setseed(0.23);
SELECT insert_random_entries();

SELECT
  to_char(start_dt, 'YYYY-MM-DD')              AS day,
  -- hours
  -- nice: http://stackoverflow.com/a/952600/241240
  extract(EPOCH FROM end_dt - start_dt) / 3600 AS hours
FROM ftt_entry;
