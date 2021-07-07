
import sys

x = sys.argv[1]

if x.isdigit():
    print("num")
elif x.isalpha():
    print("str")

s = input("what is it? ")
if s.isalpha():
    print("str")
else:
    print("num")

if s.isalpha():
    print("%s is str" % s)
else:
    print("%s is num" % s)


