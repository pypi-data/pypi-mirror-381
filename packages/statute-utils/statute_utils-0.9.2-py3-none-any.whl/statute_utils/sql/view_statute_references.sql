-- Statute titles can be used to detect future references.
-- This is a precursor to generating the statute_references table.

-- Each statute contains different names, combine them into an fts expression
WITH fts_expr AS (
  SELECT
    group_concat(
      ' "' || statute_titles.text || '" ',
      'OR'
    ) AS q
  FROM
    statute_titles
  WHERE
    (
      statute_titles.cat = 'serial'
      OR statute_titles.cat = 'short'
      OR statute_titles.cat = 'alias'
    )
    AND statute_titles.statute_id = s.id
    AND length(
      statute_titles.text
    ) > 10
    AND length(
      statute_titles.text
    ) < 100
),

-- Look for statutory units mentioning target statute via fts
matched_row_ids (id) AS (
  SELECT rowid
  FROM
    statute_units_fts(
      (
        SELECT q
        FROM
          fts_expr
      )
    )
),

-- List statute units that affect the target statute
affecting_units (ids) AS (
  SELECT su.id
  FROM
    statute_units AS su
  INNER JOIN statutes AS s1
    ON su.statute_id = s1.id
  WHERE
    su.rowid IN (
      SELECT id
      FROM
        matched_row_ids
    )
    AND su.statute_id != s.id
    AND su.material_path != '1.'
    AND s1.date > s.date
) -- List each target statute (except for acts)

SELECT
  s.id,
  (
    SELECT
      group_concat(
        ids,
        ','
      )
    FROM
      affecting_units
  ) AS unit_ids
FROM
  statutes AS s
WHERE
  s.cat != 'act'
  AND unit_ids IS NOT NULL
