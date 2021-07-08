# seq = ""
# with open("sequence.protein.2.fasta", "r") as fi:
#     for line in fi:
#         if line.startswith(">"):
#             title = line
#         else:
#             seq += line.strip()
# print(f"title: {title}")
# print(f"seq: {seq}")

# fi.read()로 풀어보기!!!!!!!★
seq = ""
with open("sequence.protein.2.fasta", "r") as fi:
    for line in fi:
        if line.startswith(">"):
            title = line
        else:
            seq += line.strip()
print(f"title: {title}")
print(f"seq: {seq}")
