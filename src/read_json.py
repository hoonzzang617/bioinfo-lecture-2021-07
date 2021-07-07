import json

with open("data.json", "r") as handle:
    data = json.load(handle)
print(data)
data1 = data[0].values()
print(data1)

for elem in data:
    print(f"{elem['id']}\t{elem['sequence']}\t{elem['species']}")
# tsv로 만들어주기
