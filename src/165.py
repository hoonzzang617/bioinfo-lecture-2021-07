l_lead = []
data = dict()
with open("061.fastq", "r") as fi:
    for line in fi:
        if line.startswith("@"):
            l_lead.append(line)


print(len(l_lead))


cnt = 0  # 이거 다시 보기 !!!!!!!!!
data = dict()
with open("061.fastq", "r") as handle:
    for line in handle:
        if cnt % 4 == 1:  # header
            pass
        elif cnt % 4 == 2:  # base
            for base in line.strip():
                if base not in data:
                    data[base] = 0
                data[base] += 1
        elif cnt % 4 == 3:  # delimiter
            pass
        elif cnt % 4 == 0:  # qual
            pass
        cnt += 1
print(cnt)
print(cnt / 4)
print(data)
