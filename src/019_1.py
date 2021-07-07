import sys


try:
    num = int(input("enter: "))
except ValueError as err:
    print(err)
    sys.exit()
try:
    print(10 / num)
except ZeroDivisionError as err:
    print(err)
    sys.exit()

'''
위에 두개를 합치는 방법

try:                        # 실행하는 것을 try로 한번에 묶어준다. 단점은 어디서 에러가 나는지 알 수 없다 
    val = int(input("enter: "))
    print(10/val)
except ZeroDivisionError as err1:
    print(err1)
    sys.exit()
except ValueError as err2:
    print(err2)
    sys.exit()
'''

