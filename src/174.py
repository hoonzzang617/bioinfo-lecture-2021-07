# l_data = []

# with open("070.vcf", "r") as fi:
#     for line in fi:
#         if line.startswith("#"):
#             continue
#         l_data.append(line)

# print(len(l_data))

# print(l_data)
# x = "".join(l_data)
# print(x.count("PASS"))

# cnt = 0
# for i in l_data:
#     if "PASS" in i:
#         cnt += 1
# print(cnt)

cnt_all = 0
cnt_pass = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[6] == "PASS":
            cnt_pass += 1
print(cnt_pass, cnt_all, cnt_pass / cnt_all)

cnt_all = 0
cnt_pass = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            # if data[6] == "PASS":
            cnt_pass += 1
print(cnt_pass, cnt_all, cnt_pass / cnt_all)
