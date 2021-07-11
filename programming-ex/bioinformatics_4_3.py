seq_list = []
origin = False
with open("sequence.protein.gb", "r") as fi:
    print("title:", fi.readline().strip())
    for line in fi:
        line = line.strip()
        if line == "":
            continue
        elif line[:6] == "ORIGIN":
            origin = True
        elif origin == True:
            seq_list.append(line)
# print(seq_list)   확인용
seq = "".join(seq_list)
# print(f"seq: {seq}")

seq_list2 = []
for i in seq:
    if i.isdigit():
        pass
    elif i.isalpha():
        seq_list2.append(i)

# print(seq_list2)
seq2 = "".join(seq_list2)

# print(f"seq: {seq2}")

# seq_list3 = []
# num = 0
# for x in seq2:
#     seq_list3.append(seq2[num : num + 70])
#     num += 70

# seq3 = "\n".join(seq_list3)
# print(seq3)

seq_list3 = []
num = 0
while True:
    seq_list3.append(seq2[num : num + 70])
    num += 70
    if num > len(seq2):
        break

seq3 = "\n".join(seq_list3)
print(seq3)
