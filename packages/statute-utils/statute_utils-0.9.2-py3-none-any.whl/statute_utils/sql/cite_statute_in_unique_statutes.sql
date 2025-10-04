-- target: statute
-- is: mentioned
-- by: unique statute in the future
-- mentions: number of times such future statute refers to target
select
  base_ref.statute_id as target,
  su1.statute_id as id,
  su1.date,
  (
    select v.text
    from
      statute_titles as v
    where
      v.cat = 'serial'
      and v.statute_id = su1.statute_id
  ) as serial_title,
  (
    select v.text
    from
      statute_titles as v
    where
      v.cat = 'official'
      and v.statute_id = su1.statute_id
  ) as official_title,
  (
    select v.text
    from
      statute_titles as v
    where
      v.cat = 'short'
      and v.statute_id = su1.statute_id
  ) as short_title,
  count(su1.statute_id) as mentions
from
  statute_references as base_ref
inner join statute_units as su1 on base_ref.affector_statute_unit_id = su1.id
inner join statute_titles as st on su1.statute_id = st.statute_id
group by
  su1.statute_id
order by
  su1.date desc, su1.statute_id asc
