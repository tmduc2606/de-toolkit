-- Basic example of performing for-loop to print value if it's not equal
-- to McIntosh, otherwise print f"I hate {i}"

{% set apples = ["Gala", "Red Delicious", "Fuji", "McIntosh", "Honeycrisp"] %}

{% for i in apples %}

    {% if i != "McIntosh" %}
        {{ i }}
    {% else %}
        I hate {{ i }}    
    {% endif %}

{% endfor %}