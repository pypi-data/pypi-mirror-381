-- target: statute
-- is: mentioned
-- by: statute units in the future
select
  sr.statute_id as target,
  su.id,
  su.item,
  su.caption,
  su.content,
  su.material_path,
  su.statute_id,
  st.text as serial,
  su.date
from
  statute_references as sr
inner join statute_units as su on sr.affector_statute_unit_id = su.id
inner join
  statute_titles as st
  on su.statute_id = st.statute_id and st.cat = 'serial'
order by
  target desc, su.date desc
