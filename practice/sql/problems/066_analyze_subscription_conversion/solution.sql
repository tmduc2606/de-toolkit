-- Optimal approach: LAG() builds the previous-activity context per user;
-- ConvertedUser keeps only users whose free_trial was immediately followed
-- by a paid subscription; the final query averages activity_duration per
-- activity type with ROUND(..., 2)
WITH Activity AS (
    SELECT
        ua.user_id,
        ua.activity_date,
        ua.activity_type,
        LAG(ua.activity_type) OVER (
            PARTITION BY ua.user_id
            ORDER BY ua.activity_date
        ) AS previous_type,
        ua.activity_duration
    FROM UserActivity ua
),
ConvertedUser AS (
    SELECT DISTINCT user_id
    FROM Activity
    WHERE previous_type = 'free_trial' AND activity_type = 'paid'
)
SELECT
    a.user_id,
    ROUND(AVG(
        CASE WHEN a.activity_type = 'free_trial' THEN a.activity_duration END
    ), 2) AS trial_avg_duration,
    ROUND(AVG(
        CASE WHEN a.activity_type = 'paid' THEN a.activity_duration END
    ), 2) AS paid_avg_duration
FROM Activity a
JOIN ConvertedUser cu ON a.user_id = cu.user_id
GROUP BY a.user_id
ORDER BY a.user_id;