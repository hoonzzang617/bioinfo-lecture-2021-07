seq = ""
with open("sequence.protein.2.fasta", "r") as fi:
    for line in fi:
        if line.startswith(">"):
            title = line
        else:
            seq += line.strip()

print(list(seq))


while True:
    x = input("Position: ")
    if x == "XXX":
        print("Okay, I will stop")
        break
    elif (int(x) + 1) > len(seq):
        print("Position is out of range")
    else:
        print(f"Three amino acids: {seq[int(x)-1:int(x)+2]}")
