# "%-8.2f": - means left-aligned, 8 means placeholder length, .2 means decimal count, f means float
my_height = 180 # cm
my_height_inch = my_height * 0.39370
print("He's %-8r cm  / %-8.2f inch tall." % (my_height, my_height_inch))

#Change the code to one line.
#Copy the content from one file to another file
open('mew-file.txt', 'w').write(open('text.txt').read())