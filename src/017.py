file_name = "write_sample.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n") #끝에 \n을 안 쓰게 되면 프롬프트가 바로 붙어서 나온다

wiht open(file_name, "a") as handle:  #"a"는 끝에 추가, "w"는 삭제하고 다시 시작한다
    handle.write("sunny\n")

s = "s1,s2,s3"  #csv / :set list 로 하면 공백이 보인다 지울때는 :set nolist
#s1 = "s1    s2  s3" #tsv
data = s.split(",")  #tsv는 \t로 나눈다
print(data)  #["s1", "s2", "s3"]

with open(file_name, "a")
    handle.write("\t".join(data))  # ,로 나눠진 scv를 tap으로 이어진 tsv로 만들어준다 
