def count_nucleotides(dna):
    a_count = dna.count('A')
    c_count = dna.count('C')
    g_count = dna.count('G')
    t_count = dna.count('T')
    return f"{a_count} {c_count} {g_count} {t_count}"

# Sample input
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_nucleotides(dna))
