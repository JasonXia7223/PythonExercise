from sys import argv

# script, filename = argv

# txt = open(filename)

# print("Here's your file %r:" %filename)
# print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again, 'a+')

txt_again.write("\nThis string is added by Python.")

print(txt_again.tell())

txt_again.seek(0, 0)

print(txt_again.read())

txt_again.close()