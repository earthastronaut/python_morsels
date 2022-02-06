WITH hacker_date AS (
    SELECT hacker_id,
        submission_date,
        COUNT(submission_id) as submission_cnt
    FROM Submissions 
    -- WHERE hacker_id in (463, 650, 8878)
        -- 463  2016-03-13 to 14
        -- 650 2016-03-01 to 15
        -- 8878 2016-03-01 to 03, 11
        -- 11587 2016-03-01
    GROUP BY hacker_id,
        submission_date -- 35 total
),
hacker_date_with_date_lag AS (
    SELECT hacker_id,
        submission_date,
        submission_cnt,
        (
            LAG(submission_date) OVER (
                PARTITION BY hacker_id
                ORDER BY submission_date ASC
            )
        ) AS submission_date_lag
    FROM hacker_date
),
hacker_date_with_lag_ctr AS (
    SELECT hacker_id,
        submission_date,
        submission_cnt,
        CASE
            WHEN submission_date_lag IS NULL THEN 1
            WHEN DATEDIFF(day, submission_date_lag, submission_date) = 1 THEN 1
            ELSE 0
        END AS hacker_date_lag_ctr
    FROM hacker_date_with_date_lag
),
hacker_date_with_days_sum AS (
    SELECT hacker_id,
        submission_date,
        submission_cnt,
        DATEDIFF(day, '2016-03-01', submission_date) + 1 AS days_since_start,
        SUM(hacker_date_lag_ctr) OVER (
            PARTITION BY hacker_id
            ORDER BY submission_date
        ) AS days_sum
    FROM hacker_date_with_lag_ctr
),
date_with_hacker_count AS (
    SELECT submission_date,
        SUM(
            CASE
                WHEN days_since_start = days_sum THEN 1
                ELSE 0
            END --AS days_continuous_ctr
        ) AS hacker_unique_cnt
    FROM hacker_date_with_days_sum
    GROUP BY submission_date
),
date_with_max_submissions AS (
    SELECT DISTINCT hd.submission_date -- , hd.submission_cnt
        -- , h.hacker_id
        -- , h.name
,
        FIRST_VALUE(h.hacker_id) OVER (
            PARTITION BY hd.submission_date
            ORDER BY hd.submission_cnt DESC,
                hd.hacker_id ASC
        ) AS hacker_id_with_max_cnt,
        FIRST_VALUE(h.name) OVER (
            PARTITION BY hd.submission_date
            ORDER BY hd.submission_cnt DESC,
                hd.hacker_id ASC
        ) AS hacker_name_with_max_cnt
    FROM hacker_date hd
        JOIN Hackers h ON h.hacker_id = hd.hacker_id 
        -- WHERE submission_date in ('2016-03-03', '0006-03-01')
        -- ORDER BY hd.submission_date, hd.submission_cnt DESC, hd.hacker_id ASC
)
SELECT dh.submission_date,
    dh.hacker_unique_cnt,
    ds.hacker_id_with_max_cnt,
    ds.hacker_name_with_max_cnt
FROM date_with_hacker_count dh
    JOIN date_with_max_submissions ds ON dh.submission_date = ds.submission_date