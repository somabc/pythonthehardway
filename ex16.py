# import filesystem commands
from sys import argv
# Set two variables as command line arguments
script, filename = argv
# print variable filename to screen message along with instructions
print "We're going to erase %r." % filename
print "If you don't want to do that hit CTRL-C (^C)."
print "If you do want that hit RETURN."
# Ask user for input to continue
raw_input("?")
# Open the file with write access from the specified variable
print "Opening the file..."
target = open(filename, 'w')
# Truncate the file
print "Truncating the file. Goodbye!"
target.truncate()
# Ask for input (3 variables)
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# Write the variables to the file 
print "I'm going to write these to a file."
# write each inputed variable with a new line
target.write(str(line1) + '\n' + str(line2) + '\n' + str(line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
# close the file
print "And finally, we close it."
target.close()