SELECT * FROM {{ ref('mapping') }}

-- source() macro is only used for tables defined as dbt sources in a sources: block of a YAML file.
-- use ref() instead for seeds.