# Load argument module from sys
from sys import argv

# use script and filename as runtime arguments
script, filename = argv

# open the file with runtime argument 'filename' and assign function txt
txt = open(filename)

# prints the filename then prints the contents if the file using the read command
print "Here's your file %r:" % filename
print txt.read()

# close the file
txt.close()

# Asks for the filename again using raw_input
print "I'll also ask you to type it again:"
file_again = raw_input ("> ")

# Assigns filename to function
txt_again = open(file_again)

# prints the contents of the file using the read command
print txt_again.read()

# close the file
txt_again.close()