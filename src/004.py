
import sys

if len(sys.argv) != 2:
    print(f"usage: python {sys.argv[0]} {num}")
    sys.exit()

num = int(sys.argv[1])

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")


result = "odd"   #else 안쓰고 하는 법, 미리 변수로 디폴트값을 정해놓고 if에 해당하지 않으면 디폴트 값이 나오고 if에 참이라면 변수를 새로 할당해주는
if num % 2 == 0:
    result="짝수"
print(result)






