-- target: statute
-- is: a component of
-- by: codifications
select
  cs.statute_id as target,
  c.id,
  c.title,
  c.date,
  (
    select text
    from
      statute_titles
    where
      cat = 'serial'
      and statute_id = s.id
  ) as serial,
  (
    select text
    from
      statute_titles
    where
      cat = 'official'
      and statute_id = s.id
  ) as official
from
  codification_statutes as cs
inner join codifications as c on cs.codification_id = c.id
inner join statutes as s
  on
    c.cat = s.cat
    and c.num = s.num
group by cs.statute_id, cs.codification_id
