seq = ""
with open("sequence.protein.2.fasta", "r") as fi:
    for line in fi:
        if line.startswith(">"):
            title = line
        else:
            seq += line.strip()

print(seq)

# s_seq = "".join(seq)
i = 0
position_res = ""
while True:
    request = input("Searching for: ")
    if request == "XXX":
        print("Okay, I will stop")
        break
    else:
        for base in seq:
            position_res += str(seq.find(request, i))
            i += 1
    print(position_res)
