x = 7**6
print x

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

