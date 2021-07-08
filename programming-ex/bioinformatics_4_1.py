# cnt = 0
# fi = open('sequence.protein.gb', 'r')
# for line in fi:
#     cnt += 1
#     if line.startswith('ORIGIN'):
# fi.close()
line = []
with open("sequence.protein.gb", "r") as fi:
    print(fi.readline())
    line = fi.readlines()
    if line.startswith("ORIGIN"):
        pass
    x = line.strip()
print(x)
