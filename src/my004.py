

num1 = int(input("숫자입력"))

if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")




import sys


if len(sys.argv) != 2:
    print(f"#usage : python {sys.argv[0]} [n1]")
    sys.exit()
num = int(sys.argv[1])

if num % 2 == 0:
    print("even")
else:
    print("odd")





