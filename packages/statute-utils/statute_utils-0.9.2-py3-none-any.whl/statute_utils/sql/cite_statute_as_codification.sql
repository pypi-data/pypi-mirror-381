select
  s.id as target,
  c.id,
  json_group_array(
    json_object(
      'id',
      cs.statute_id,
      'date',
      cs.date,
      'subtitle',
      (
        select text
        from
          statute_titles
        where
          statute_id = cs.statute_id
          and cat = 'serial'
      ),
      'title',
      (
        coalesce(
          (
            select text
            from
              statute_titles
            where
              statute_id = cs.statute_id
              and cat = 'short'
          ),
          (
            select text
            from
              statute_titles
            where
              statute_id = cs.statute_id
              and cat = 'official'
          )
        )
      )
    )
    order by cs.date desc
  ) as components
from
  codification_statutes as cs
inner join codifications as c on cs.codification_id = c.id
inner join statutes as s
  on
    c.cat = s.cat
    and c.num = s.num
group by
  c.id
