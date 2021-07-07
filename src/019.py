
'''
with open("noname.txt", "r") as fr:
    read = fr.readlines()
'''
#파일이 없을때 에러가 나오기 전에 예상을 해서 미리 오류를 잡는
try:
    with open("noname.txt". "r") as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print("파일이 없음")   #print(err)
    sys.exit()

print(data)



print(10 / num)


