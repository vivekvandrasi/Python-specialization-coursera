filename = raw_input('Enter file name: ')
fhandle = open(filename)

count=0
conf = 0
for line in fhandle:
    line = line.rstrip()
    if 'X-DSPAM-Confidence' in line:
        count = count + 1
        index = line.find(':')
        conf = conf + float(line[index+1:])

average = conf / count
print "Average spam confidence:",average
