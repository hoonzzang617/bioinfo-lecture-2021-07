# 해당하는 문자가 어디어디 있는지 찾는 문제

from types import new_class


seq = ""
with open("sequence.protein.2.fasta", "r") as fi:
    for line in fi:
        if line.startswith(">"):
            title = line
        else:
            seq += line.strip()

print(seq)
l_seq = list(seq)

# s_seq = "".join(seq)

i = 0


while True:
    position_res = []
    request = input("Searching for: ")
    if request == "XXX":
        print("Okay, I will stop")
        break
    # else:
    while True:
        # for base in seq:
        if seq.find(request, i) == -1:
            break
        # elif base == request:
        else:
            position_res.append(seq.find(request, i) + 1)
            # += str(seq.find(request, i))
            i = seq.find(request, i) + 1
    print(position_res)
