import re

fhandle = open('regex_sum_265618.txt')

str = fhandle.read()

lst = re.findall('[0-9]+',str)

print sum([int(i) for i in lst])
