l_lead = []
with open("061.fastq", "r") as fi:
    for line in fi:
        if line.startswith("@"):
            l_lead.append(line)


print(len(l_lead))

cnt = 0
with open("061.fastq", "r") as fi:
    for line in fi:
        if line.startswith("@"):
            cnt += 1
print(cnt)

d_base = dict()
cnt1 = 0
with open("061.fastq", "r") as file:
    for line3 in file:
        cnt1 += 1
        if cnt1 % 4 == 0:
            continue
        elif cnt1 % 4 == 1:
            for base in line3.strip():
                if base not in d_base:
                    d_base[base] = 1
                d_base[base] += 1
        elif cnt1 % 4 == 2:
            continue
        elif cnt1 % 4 == 3:
            continue
print(d_base)


# cnt = 0  # 이거 다시 보기 !!!!!!!!!
# data = dict()
# with open("061.fastq", "r") as handle:
#     for line in handle:
#         if cnt % 4 == 0:  # header
#             pass
#         elif cnt % 4 == 1:  # base
#             for base in line.strip():
#                 if base not in data:
#                     data[base] = 0
#                 data[base] += 1
#         elif cnt % 4 == 2:  # delimiter
#             pass
#         elif cnt % 4 == 3:  # qual
#             pass
#         cnt += 1
# print(cnt)
# print(cnt / 4)
# print(data)
