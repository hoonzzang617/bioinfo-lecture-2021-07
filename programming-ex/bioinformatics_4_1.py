# cnt = 0
# fi = open('sequence.protein.gb', 'r')
# for line in fi:
#     cnt += 1
#     if line.startswith('ORIGIN'):
# fi.close()

# x = ""
# with open("sequence.protein.gb", "r") as fi:
#     print("title:", fi.readline())
#     for line in fi.readline():
#         if line.startswith("ORIGIN"):
#             pass
#         else:
#             for seq in line:
#                 x += seq

# print(x)


# with open("sequence.protein.gb", "r") as fi:
#     print("title:", fi.readline())
#     x = fi.readlines
#     for seq in x:
#         if x.startswith("ORIGIN"):
#             pass
#         else:
#             for

seq_list = []
origin = False
with open("sequence.protein.gb", "r") as fi:
    print("title:", fi.readline().strip())
    for line in fi:
        line = line.strip()
        if line == "":
            continue
        elif line[:6] == "ORIGIN":  # 여기가 참이면 밑에 elif 참 거짓 검사 안한다
            origin = True
        elif origin == True:
            seq_list.append(line)
# print(seq_list)
seq = "\n".join(seq_list)
print(f"seq: {seq}")
