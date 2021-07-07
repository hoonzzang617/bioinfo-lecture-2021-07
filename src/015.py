import sys

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit()

s= sys.argv[1]

print(f"Hello, {s}.")

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)
num = int(sys.argv[1])
try:
    res = 10 / num
except ZeroDivisionError:
    sys.exit(2)        #프로그래머가 echo $ 했을때 나오는 숫자에 해당하는 오류를 정해줄 수 있다. = 에러코드
print(res)

'''
if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)
num = int(sys.argv[1])
try:
    res = 10 / num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2) 
print(res)
'''

''' # num에 정수가 아니라 a를 넣어준 경우
if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)
try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)
try:
    res = 10 / num
except ZeroDivisionErrora as err:
    print(err)
    sys.exit(2) 
print(res)
'''
