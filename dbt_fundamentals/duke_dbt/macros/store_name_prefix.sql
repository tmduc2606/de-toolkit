{% test store_name_prefix(model, column_name, prefix) %}

select *
from {{ model }}
where {{ column_name }} not like '{{ prefix }} %'

{% endtest %}