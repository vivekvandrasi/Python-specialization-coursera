fhandle = open('mbox-short.txt')

counts = dict();
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        counts[hour] = counts.get(hour,0) + 1

for k, v in sorted(counts.items()):
    print k, v

print sorted([(v,k) for k,v in counts.items()])