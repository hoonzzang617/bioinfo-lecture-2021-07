d_base = dict()
while True:
    x = input("Enter three-base codon to build: ")
    if x == "XXX":
        print("Okay, I will switch.")
        break
    else:
        y = input("Enter amino acid: ")
        d_base[x] = y

while True:
    z = input("Enter three-base codon to search: ")
    if z == "XXX":
        print("Okay, I will stop.")
        break
    else:
        print(f"Amino acid for {z}: {d_base[z]}")

# a = input("Enter three-base to search: ")
# b = input(f"Amino acid for {a}: ")
