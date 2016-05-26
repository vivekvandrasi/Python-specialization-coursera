fhandle = open('mbox-short.txt')

count = 0
finallist=[]
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        linelist = line.split()
        print linelist[1]
        count = count + 1

print "There were", count, "lines in the file with From as the first word"