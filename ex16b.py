from sys import argv

script, filename = argv

print "Opening File...."
txt = open(filename)

print txt.read()
txt.close()