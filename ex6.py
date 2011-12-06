# number of people types
x = "There are %d types of people." % 10
# equal to %d
binary = "binary"
# number for binary
do_not = "don't"
# x + y
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# calls binary number
print "I said: %r." % x
# puts it all together
print "I also said: '%s'." % y

# string for answer
hilarious = False
# asks the question, gives the answer
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# variables for lines to be printed together
w = "This is the left side of..."
e = "a string with a right side."

print w + e
