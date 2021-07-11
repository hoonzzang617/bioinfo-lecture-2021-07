codon_dic = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
base_dic = {"A": "T", "T": "A", "C": "G", "G": "C"}

fi = open("sequence.nucleotide.fasta", "r")
seq = ""
for line in fi:
    if line.startswith(">"):
        continue
    seq += line.strip()
fi.close()
rev_seq = seq[::-1]
rev_com_seq = ""
num = 0
for base in seq:
    rev_com_seq += base_dic[base]
    num += 1
    if num >= len(seq):
        break

frwd_1, frwd_2, frwd_3 = "", "", ""
num_1, num_2, num_3 = 0, 1, 2
for base in seq:
    if num_1 >= len(seq):
        break
    frwd_1 += codon_dic[seq[num_1 : num_1 + 3]] + "  "
    if num_2 + 3 > len(seq):
        break
    frwd_2 += " " + codon_dic[seq[num_2 : num_2 + 3]] + " "
    if num_3 > len(seq):
        break
    frwd_3 += "  " + codon_dic[seq[num_3 : num_3 + 3]]
    num_1 += 3
    num_2 += 3
    num_3 += 3

print(frwd_1)
print(frwd_2)
print(frwd_3)
print(seq)
print(rev_com_seq)
