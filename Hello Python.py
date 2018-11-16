# x = 7**2
# print(x)

# String
# t = 'he is a string. Who are you?'
# print(t.capitalize())
# print (t.split())
# print(t.find('i'))
# print (t.find('in'))
# print(t.find('Python'))
# print(t[0:4])
# print(t.replace(' ', '|'))

# List
# classmates = ['Lily', 'Adam',' Allen', 'Sophia', 'Bob']
# # classmates.append('Jim')
# # classmates.append(['Jimmy', 'Donny'])
# # classmates.extend(['Jimmy', 'Donny'])
# classmates.insert(0, ['Jimmy', 'Donny'])
# classmates[0][1] = 'Donald'
# # classmates.remove('Adam')
# # classmates.pop(1)
# print classmates[0][1]

# Tuple
# tupleMates = ('Allen', 'Adam', ['Lily', 'Bob'])
# tupleMates[2][1] = 'Donney'
# print tupleMates

# a = [24, 54, 16]
# b = []
# if a[0] <= a[1]:
#     b.append(a[0])
#     b.append(a[1])
# else:
#     b.append(a[1])
#     b.append(a[0])
# if  a[2] <= b[0]:
#     b.insert(0, a[2])
# elif a[2] >= b[1]:
#     b.append(a[2])
# else:
#     b.insert(1, a[2])
# print a, b

# for i in range(300, 351):
#     if i % 17 == 0:
#         print i
#         break
#     else:
#         continue

# i = 300
# while i < 351:
#     if i % 17 == 0:
#         print i
#         break
#     i += 1

# sumUp = 0
# for i in range(1, 1001):
#     sumUp += i
# print sumUp
#
# sumUp = 0
# for i in range(1, 1001):
#     if i % 2 == 0:
#         sumUp += i
#     else:
#         continue
# print sumUp

# def MaxNumber(p1, p2):
#     if p1 >= p2:
#         return p1
#     else:
#         return p2
#
# a = 10
# b = 12
# c = MaxNumber(a, b)
# print c

# def x_plus_one(x1, x2, x3):
#     x1 += 1
#     x2 += 2
#     x3 += 3
#     return (x1, x2, x3)
# a1 = 1
# a2 = 2
# a3 = 3
# a1, a2, a3 = x_plus_one(a1, a2, a3)
# print a1, a2, a3

# file = open('PythonLife.txt', 'w')
# file .write('I create this file for the course. \n')
# file .write('How about you? \n')
# file.write('How is your exam?')
# file.close()

# file  = open('PythonLife.txt', 'r')
# # print(file.read())
# # print(file.read(10))
# print(file.readlines())
# file.close()

# file = open('PythonLife.txt', 'r')
# for line in file:
#     print line
# file.close()

# with open('PythonLife.txt','r') as file_obj:
#     for line in file_obj:
#         print line


# with open('C:\\Users\\v-jasxi\\Documents\\SpecificFile.txt', 'r+') as file_obj:
#     file_obj.write('Open a file through specific path! \n')
    # file_obj.write('Bravo!')

# with open('C:\\Users\\v-jasxi\\Documents\\SpecificFile.txt', 'r') as file_obj:
#     for lines in file_obj:
#         print lines
#
# amount = float(input("Enter amount: "))
# inrate = float(input("Enter interest rate: "))
# period = float(input("Enter period: "))
#
# value = 0
# year = 1
#
# while year <= period:
#     value = amount + amount * inrate
#     print("Year {} Rs. {}".format(year, value))
#     amount = value
#     year = year + 1

# data = ('urnotjason', 'China', 'Python')
# name, country, language = data
# print(name, country, language)

# sum = 0
# for i in range(1,11):
#     sum += 1 / i
#     print(sum)
#     i += 1

# import math
# radius = int(input('Please enter the radius: '))
# area = math.pi * radius ** 2
# print(('The cycle area is {:.10f}').format(area))

# a = 0
# b = 1
#
# while b < 100:
#     print(b)
#     a, b = b, a + b

# a = 1
# b = 1
#
# while a < 10:
#     while b < 10:
#         print(('{} * {} = {}').format(a, b, a * b))
#         b += 1
#     a += 1
#     b = 1

# print(bool(-123))
# print(bool(123))
# print(bool('True'))
# print(bool('False'))
# print(bool(0.1))
# print(bool(''))

# def SayHello(a):
#     print("Hello from " + a)
#
# SayHello('Jason')
#
# def BigorSmall(a, b):
#     if(a > b):
#         print(a)
#     else:
#         print(b)
#
# BigorSmall(12,6)

# print("How old are you?")
# age = int(input())
#
# print("How tall are you?")
# height = input()
#
# print("How much do you weigh?")
# weight = input()
#
# print("So you're %r old, %r tall and %r heavy" %(age, height, weight))

# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
# # print(numbers[0])
# # your code goes here
# x = -1
# while x <= len(numbers):
#     x += 1
#     if numbers[x] == 237:
#         break
#     elif numbers[x] % 2 > 0:
#         continue
#     print(numbers[x])

def myFunc(n):
    return  lambda a: a * n

myInt = myFunc(2)
print(myInt(11))