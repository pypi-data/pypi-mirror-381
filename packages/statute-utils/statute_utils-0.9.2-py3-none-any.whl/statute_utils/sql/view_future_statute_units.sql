with future_mentions (units) as (
  select
    json_group_array(
      json_object(
        'affector_locator',
        c.item,
        'affector_caption',
        c.caption,
        'affector_content',
        c.content,
        'affector_material_path',
        c.material_path,
        'affector_statute_id',
        c.statute_id,
        'affector_statute',
        c.serial,
        'affector_statute_date',
        c.date
      )
      order by
        c.date desc
    )
  from
    cite_statute_in_statute_units as c
  where
    c.target = s.id
),

interim_uniqs as (
  select
    su1.statute_id,
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
    count(su1.statute_id) as num
  from
    statute_references as sr1
  inner join statute_units as su1 on sr1.affector_statute_unit_id = su1.id
  inner join statute_titles as st on su1.statute_id = st.statute_id
  where
    sr1.statute_id = s.id
  group by
    su1.statute_id
  order by
    su1.date desc
),

uniq_statute_list (result) as (
  select
    json_group_array(
      json_object(
        'statute_id', i.statute_id, 'serial_title',
        i.serial_title, 'official_title',
        i.official_title, 'short_title',
        i.short_title, 'date', i.date, 'count',
        i.num
      )
      order by
        i.date desc
    )
  from
    interim_uniqs as i
)

select
  s.id,
  (
    select result
    from
      uniq_statute_list
  ) as unique_statutes_list,
  (
    select json_array_length(result)
    from
      uniq_statute_list
  ) as unique_statutes_list_count,
  (
    select units
    from
      future_mentions
  ) as future_statute_units,
  (
    select json_array_length(units)
    from
      future_mentions
  ) as future_statute_units_count
from
  statutes as s
where
  future_statute_units_count > 0
