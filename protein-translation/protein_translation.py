def proteins(strand):
    codons_in_strand = [strand[i:i+3] for i in range(0, len(strand), 3)]
    codons = [["AUG"], ["UUU", "UUC"], ["UUA", "UUG"], ["UCU", "UCC", "UCA", "UCG"], ["UAU", "UAC"], ["UGU", "UGC"],
              ["UGG"], ["UAA", "UAG", "UGA"]]
    amino_acids = ["Methionine", "Phenylalanine", "Leucine", "Serine", "Tyrosine", "Cysteine", "Tryptophan", "STOP"]
    ans = []
    index = 0
    while  index != len(codons_in_strand) and codons_in_strand[index] not in codons[-1]:
        for i in range(len(codons[:-1])):
            for j in codons[i]:
                if j == codons_in_strand[index]:
                    ans.append(amino_acids[i])
                    break
        index += 1
    return ans
