x = int(input("Which times tatbe: "))

if x > 9 or x < 1:
    print("What?")
else:
    for i in range(1, 10):
        print(f"{x} * {i} =", x * i)
        i += 1
