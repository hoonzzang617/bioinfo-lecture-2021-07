
import sys

if len(sys.argv) != 2:
    print(f"#usage python {sys.argv[0]} [n1]")
    sys.exit()
num1 = int(sys.argv[1])

if num1 % 3 == 0 and num1 % 7 == 0:
    print("3과 7의 배수")
elif num1 % 3 == 0:
    print("3의배수")
elif num1 % 7 == 0:
    print("7의 배수")
else:
    print("어떤 것도 아니다") 



