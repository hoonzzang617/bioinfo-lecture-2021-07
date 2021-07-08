cnt = 0
with open("sequence.protein.2.fasta", "r") as fi:
    for line in fi:
        cnt += 1
        if cnt == 2:
            print(f"The second line is: {line}")
