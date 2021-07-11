i_file = input("Enter input file: ")
o_file = input("Enter ouput file: ")
print(
    """Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file.
Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file.
Option-3) Convert GenBank format file to FASTA format file."""
)
s_option = input("Select the option: ")
base_code = {"A": "T", "T": "A", "C": "G", "G": "C"}
# seq = []
seq = ""
if s_option == str(1):
    with open(i_file, "r") as fi:
        for line in fi:
            if line.startswith(">"):
                title = line
            else:
                seq += line.strip()
    rev_seq = seq[::-1]

    with open(o_file, "w") as fil:
        fil.write(title + rev_seq)
        # print(seq)
    #             seq.append(line.strip())
    #     seq_s = "".join(seq)
    # print(seq_s)

elif s_option == str(2):
    with open(i_file, "r") as fi:
        for line in fi:
            if line.startswith(">"):
                title = line
            else:
                seq += line.strip()
    rev_seq = seq[::-1]
    rev_com_seq = ""
    for i in rev_seq:
        rev_com_seq += base_code[i]
    with open(o_file, "w") as fil:
        fil.write(title + rev_com_seq)
elif s_option == str(3):
    origin = False
    with open(i_file, "r") as fi:
        title = fi.readline()
        for line in fi:
            line = line.strip()
            if line == "":
                continue
            elif line[:6] == "ORIGIN":
                origin = True
            elif origin == True:
                seq += line
    gb_seq = ""
    for i in seq:
        if i.isdigit():
            continue
        elif i.isalpha():
            gb_seq += i
    with open(o_file, "w") as fil:
        fil.write(">" + title + gb_seq)

# rev_seq += base_code[i]
