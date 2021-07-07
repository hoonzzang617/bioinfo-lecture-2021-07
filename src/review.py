import gzip
with gzip.open("covid19.fasta.gz", "rb") as f:   #rb는 바이너리 모드로 읽는
   #rb로 할 경우에는 line = line.decode("utf-8")이 추가되어야 한다. 
    print(f.readlines())
    a = f.readlines()
    print(a.count("A"))
    print(list(a))
    
file_name = "covid19.fasta"
data = dict()  #data={}
with open(file_name, 'r') as handle:
    for line in handle:
        if line.startswith(">"):  # >가 나오면 그 다음줄것
            continue
    for base in line.strip(): # 문자 하나 하나가 나온다
        if base not in data:
            data[base] = 0
        data[base] += 1
print(data)

#gzip 자체로 읽는법

file_name = "covid19.fasta.gz"
data = dict()  #data={}
with gzip.open(file_name, 'rt') as handle:   #rt가 텍스트 모드로 읽는
    for line in handle:
        if line.startswith(">"):  # >가 나오면 그 다음줄
            continue
    for base in line.strip(): # 문자 하나 하나가 나온다
        if base not in data:
            data[base] = 0
        data[base] += 1
print(data)


