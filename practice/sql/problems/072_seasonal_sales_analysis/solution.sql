-- solution.sql — Seasonal Sales Analysis (LeetCode 3564), hand-solved.
-- DuckDB: MySQL "#" line comments are not supported here -> "--".
-- DuckDB: MySQL double-quoted string literals ("Spring") parse as identifiers
--         in DuckDB -> single quotes ('Spring').
-- The trailing ORDER BY season ASC fulfills the statement requirement
-- ("Return the result table ordered by season in ascending order").

-- Group by the pairs (season, category) sales
WITH season_sales AS (
    SELECT
        (
            CASE
                WHEN MONTH(s.sale_date) >= 3 AND MONTH(s.sale_date) < 6 THEN 'Spring'
                WHEN MONTH(s.sale_date) >= 6 AND MONTH(s.sale_date) < 9 THEN 'Summer'
                WHEN MONTH(s.sale_date) >= 9 AND MONTH(s.sale_date) < 12 THEN 'Fall'
                ELSE 'Winter'
            END
        ) AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY (
            CASE
                WHEN MONTH(s.sale_date) >= 3 AND MONTH(s.sale_date) < 6 THEN 'Spring'
                WHEN MONTH(s.sale_date) >= 6 AND MONTH(s.sale_date) < 9 THEN 'Summer'
                WHEN MONTH(s.sale_date) >= 9 AND MONTH(s.sale_date) < 12 THEN 'Fall'
                ELSE 'Winter'
            END
    ), p.category
),

-- Classify the ranks of most popular categories
-- quantity -> revenue -> lexicographic
ranked AS (
    SELECT
        season,
        category,
        total_quantity,
        total_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY season
            ORDER BY
                total_quantity DESC,
                total_revenue DESC,
                category ASC
        ) AS rn
    FROM season_sales
)

-- Filter out the popular categories
SELECT
    season,
    category,
    total_quantity,
    total_revenue
FROM ranked
WHERE rn = 1
ORDER BY season ASC;
