# import argv module
from sys import argv

# unpack argv and assign to vars
script, filename = argv

# opens a txt file
txt = open(filename)

# echo back filename
print "Here's your file %r:" % filename
# echo back contents of the txt file
print txt.read()

# closes the file
txt.close()

# prompts for the filename again
print "I'll also ask you to type it again:"
file_again = raw_input("> ")

# open the file again for reading
txt_again = open(file_again)

# echo the file again
print txt_again.read()

# close the file again
txt.close()
