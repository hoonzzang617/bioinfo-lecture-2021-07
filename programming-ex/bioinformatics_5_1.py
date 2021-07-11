fi = open("sequence.nucleotide.fasta", "r")
seq = ""
for line in fi:
    if line.startswith(">"):
        continue
    seq += line.strip()
fi.close()

n = 0

for base in seq:
    if n >= len(seq):
        break
    print(seq[n : n + 3])
    n += 3
