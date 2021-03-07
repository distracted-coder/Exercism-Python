def to_rna(dna_strand):
    code = {"G": "C",
            "C": "G",
            "T": "A",
            "A": "U"}
    ans = ""
    for i in dna_strand:
        ans += code[i]
    return ans


print(to_rna("ACGTGGTCTTAA"))