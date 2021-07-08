x = ""
with open("059.fasta", "r") as fi:
    for i in fi:
        if i.startswith(">"):
            continue
        x += i.strip()
print(x.count("A"))
a = x.count("A")
t = x.count("T")
g = x.count("G")
c = x.count("C")
print(f"A : {a}, T : {t}, G : {g}, C : {c}")

d_data = dict()

with open("059.fasta", "r") as file:
    for line in file:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in d_data:
                d_data[base] = 0
            d_data[base] += 1
print(d_data)


# data = dict()
# with open("059.fasta", "r") as handle:
#     for line in handle:
#         if line.startswith(">"):
#             continue
#         for base in line.strip():
#             if base not in data:
#                 data[base] = 0
#             data[base] += 1

# print(data)
