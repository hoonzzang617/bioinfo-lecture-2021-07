

import sys  #sys.argv[]

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()

n=int(sys.argv[1])

result = n**2*3.14
print(result)


