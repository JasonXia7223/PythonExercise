i = 0
numbers = []

# while i < 6:
#     print("At the top i is %d" %i)
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now:", numbers)
#     print("At the bottom i is %d" % i)

def addNum(n, x):
    for i in range(0, n, x):
        numbers.append(i)

print("The numbers: ")

addNum(13, 2)

for num in numbers:
    print(num)


