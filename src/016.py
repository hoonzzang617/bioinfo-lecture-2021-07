
file_name = "read_sample.txt"

with open(file_name, "r") as handle:   #with open 하면 as로 객체로 받을 수 있고 for 문으로 한줄씩 받아올 수 있다.
    for line in handle:
        print(line, end="") #print(line.strip()) 기존의 텍스트 파일에 엔터가 하나 있고 print 자체에도 엔터가 하나 있기 때문에 이렇게 엔터하나를 없애준다
'''
handle = open(file_name, "r")
for line in handle:
    print(line.strip())
handle.close()     # with open으로 할시에는 for문에 인덴트가 들어가기 때문에 줄이 길어질때 이렇게 함 ★ 무조건 닫아줘야함! ★
'''
'''
handle = open(file_name, "r")
lines = handle.readlines()  #이렇게하면 리스트같은게 생긴다
for line in lines:
    print(line.strip())
handle.close()
'''
'''
with open(file_name, "r") as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.strip())
'''


