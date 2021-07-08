with open("sequence.protein.fasta", "r") as fi:
    x = fi.read()

with open("sequence.protein.2.fasta", "w") as fil:
    fil.write(x)


# 전체를 읽어서 넣는게 아니라 하나씩 읽어서 지정한 뒤에 새로운 파일에 넣기. 그리고 join 함수 사용하기
