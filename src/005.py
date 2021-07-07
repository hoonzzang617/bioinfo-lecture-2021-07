



import sys

n1 = int(sys.argv[1])
result = "neither 3,7"
if n1 % 3 == 0 and n1 % 7 ==0:
    result = "3,7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"
print(result)


