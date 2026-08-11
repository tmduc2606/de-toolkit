# SQL065 — DNA Pattern Recognition

> Source: LeetCode 3475 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Samples`

| Column Name | Type |
|---|---|
| sample_id | int |
| dna_sequence | varchar |
| species | varchar |

`sample_id` is the unique key. Each row holds a DNA sequence (characters
`A`, `T`, `G`, `C`) and the species it was collected from. Flag each sample
with `1`/`0` for:

- `has_start` — sequence starts with `ATG` (start codon)
- `has_stop` — sequence ends with `TAA`, `TAG`, or `TGA` (stop codons)
- `has_atat` — sequence contains the motif `ATAT`
- `has_ggg` — sequence has at least 3 consecutive `G` (like `GGG` or `GGGG`)

Return the result table ordered by `sample_id` in ascending order.

## Solution (MySQL, annotated)

```sql
-- LIKE patterns per rule; CASE WHEN maps each boolean to a 1/0 flag
-- has_start: begins with ATG | has_stop: ends with TAA, TAG or TGA
-- has_atat: contains ATAT  | has_ggg: contains at least GGG
SELECT
    s.sample_id,
    s.dna_sequence,
    s.species,
    (CASE WHEN s.dna_sequence LIKE 'ATG%' THEN 1 ELSE 0 END) AS has_start,
    (CASE WHEN
        s.dna_sequence LIKE '%TAA' OR
        s.dna_sequence LIKE '%TAG' OR
        s.dna_sequence LIKE '%TGA' THEN 1 ELSE 0 END) AS has_stop,
    (CASE WHEN s.dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END) AS has_atat,
    (CASE WHEN s.dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END) AS has_ggg
FROM Samples s
ORDER BY s.sample_id ASC;
```

> DuckDB note: plain `LIKE` patterns are used instead of MySQL's `REGEXP`
> (`TAA$|TAG$|TGA$` / `GGG+`) — like-wildcards are fully portable and give
> the same flags (`%GGG%` implies ≥ 3 consecutive G).

## Test-case annotations

```
Input:
Samples table:
+-----------+------------------+-----------+
| sample_id | dna_sequence     | species   |
+-----------+------------------+-----------+
| 1         | ATGCTAGCTAGCTAA  | Human     |
| 2         | GGGTCAATCATC     | Human     |
| 3         | ATATATCGTAGCTA   | Human     |
| 4         | ATGGGGTCATCATAA  | Mouse     |
| 5         | TCAGTCAGTCAG     | Mouse     |
| 6         | ATATCGCGCTAG     | Zebrafish |
| 7         | CGTATGCGTCGTA    | Zebrafish |
+-----------+------------------+-----------+

Sample 1: starts ATG, ends TAA → has_start 1, has_stop 1; no ATAT/GGG.
Sample 2: contains GGG → has_ggg 1 only.
Sample 3: contains ATAT → has_atat 1 only.
Sample 4: starts ATG, ends TAA, contains GGGG → start/stop/ggg 1.
Sample 5: no patterns.
Sample 6: ends TAG, starts with ATAT → has_stop 1, has_atat 1.
Sample 7: no patterns.

Output (ordered by sample_id ASC):
+-----------+------------------+-----------+-----------+----------+----------+----------+
| sample_id | dna_sequence     | species   | has_start | has_stop | has_atat | has_ggg  |
+-----------+------------------+-----------+-----------+----------+----------+----------+
| 1         | ATGCTAGCTAGCTAA  | Human     | 1         | 1        | 0        | 0        |
| 2         | GGGTCAATCATC     | Human     | 0         | 0        | 0        | 1        |
| 3         | ATATATCGTAGCTA   | Human     | 0         | 0        | 1        | 0        |
| 4         | ATGGGGTCATCATAA  | Mouse     | 1         | 1        | 0        | 1        |
| 5         | TCAGTCAGTCAG     | Mouse     | 0         | 0        | 0        | 0        |
| 6         | ATATCGCGCTAG     | Zebrafish | 0         | 1        | 1        | 0        |
| 7         | CGTATGCGTCGTA    | Zebrafish | 0         | 0        | 0        | 0        |
+-----------+------------------+-----------+-----------+----------+----------+----------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/065_dna_pattern_recognition -v` green