

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
d = dict()

for i in l:
    if i not in d:
        d[i] = 0
        d[i] += 1
    elif i in d:
        d[i] += 1
print(d)





