fhandle = open('romeo.txt')

finallist=[]
for line in fhandle:
    linelist = line.rstrip().split()
    for item in linelist:
        if item not in finallist:
            finallist.append(item)

finallist.sort()
print finallist