title = ""
with open("sequence.nucleotide.gb", "r") as fi:
    for line in fi:
        line = line.lstrip()
        if line.startswith("TITLE"):
            title += line.strip("TITLE")
print(title)
