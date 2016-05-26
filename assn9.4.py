fhandle = open('mbox-short.txt')

counts = dict();
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        emailid = line.split()[1]
        counts[emailid] = counts.get(emailid,0) + 1

maxcount = None
maxkey = None
for key,val in counts.items():
    if maxcount is None or val > maxcount:
        maxcount = val;
        maxkey = key;

print maxkey, maxcount
