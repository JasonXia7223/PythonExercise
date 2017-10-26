# from sys import argv
# from os.path import exists

# script , from_file, to_file = argv
#
# print("Copying from %s to %s" %( from_file, to_file))
#
# # we could do there two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
# # indata = open(from_file).read()
#
# print("The input file is %d byte long" %len(indata))
#
# print("Does the output file exist? %r" %exists(to_file))
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input(">")
#
# out_file = open(to_file, 'w+')
# out_file.write(indata)
# # open(to_file, 'w').write(indata)
#
# out_file.seek(0, 0)
#
# print("Alright, all done.")
# print(out_file.read())
#
# out_file.close()
# in_file.close()

open('mew-file.txt', 'w').write(open('text.txt').read())