from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", int(first))
print("Your second variable is:", int(second))
print("Your third variable is:", int(third))

a = input("please input a number:")

print(a + int(first))