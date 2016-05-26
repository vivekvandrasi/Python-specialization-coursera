filename = raw_input('Enter file name: ')
fhandle = open(filename)

for line in fhandle:
    line = line.rstrip().upper()
    print line
