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