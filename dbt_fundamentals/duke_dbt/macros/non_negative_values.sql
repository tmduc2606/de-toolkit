{% test non_negative_values(model, gross_column, net_column) %}

select *
from {{ model }}
where {{ gross_column }} < 0 and {{ net_column }} < 0

{% endtest %}
