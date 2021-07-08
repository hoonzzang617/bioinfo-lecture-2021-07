# x = input("Enter a string: ")

# print("The string legnth is", len(x))


def my_len(string):
    cnt = 0
    for i in string:
        cnt += 1
    return cnt


message = input("Enter a string: ")

y = my_len(message)
print(f"The string length is {y}.")


# def my_len(string):
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return cnt


# message = input("Enter a string: ")
# length = my_len(message)
# print("The string length is %d." % length)
