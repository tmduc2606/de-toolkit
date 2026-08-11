-- schema.sql — DNA Pattern Recognition (LeetCode 3475)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Samples (
    sample_id INTEGER PRIMARY KEY,
    dna_sequence TEXT,
    species TEXT
);

INSERT INTO Samples (sample_id, dna_sequence, species) VALUES
    (1, 'ATGCTAGCTAGCTAA', 'Human'),
    (2, 'GGGTCAATCATC', 'Human'),
    (3, 'ATATATCGTAGCTA', 'Human'),
    (4, 'ATGGGGTCATCATAA', 'Mouse'),
    (5, 'TCAGTCAGTCAG', 'Mouse'),
    (6, 'ATATCGCGCTAG', 'Zebrafish'),
    (7, 'CGTATGCGTCGTA', 'Zebrafish');