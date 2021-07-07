#! /usr/bin/env python

r=input("반지름 길이를 입력")
circle = int(r)*int(r)*3.14
print(circle)

import math
r = 2
pi = math.pi
print(r**2*pi)


import sys
r = int(sys.argv[1])  #밖에서 받아올때는 인트로 받아와야함
pi = math.pi
result = round(r**2*pi, 2)
print(result)

