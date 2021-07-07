# l_seq = []

# with open("077.bed", "r") as fi:
#     for line in fi:
#         l_seq.append(line)
# print(l_seq)

# for i in l_seq:
#     x = i.split("\t")

# print(x)
result = 0
with open("077.bed", "r") as handle:
    for line in handle:
        data = line.strip().split("\t")
        # int(data[2]) -int(data[1])
        chrom, start, end = data
        length = int(end) - int(start)
        result += length
print(result)
