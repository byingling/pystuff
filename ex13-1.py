from sys import argv

script, first, last = argv

print "Hello, %r." % first
middle = raw_input("Do you have a middle name?")
print "Hello, %r %r %r. My name is %r." % (first, middle, last, script)
