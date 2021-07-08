s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

# if int(s1) % 2 == 1 and len(s1) < len(s2):
#     print(f"{s1}" + s2)
# else:
#     print(s2 + s1)
#  이거는 s1이 홀수냐고 문제를 잘못읽어서

if (len(s1) % 2) == 1 and len(s1) < len(s2):
    print(s1 + s2)
else:
    print(s2 + s1)
