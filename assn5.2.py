smallest = None
while True:
    inp = raw_input("Enter an integer: ")
    if inp == "done":
        break
    try:
        input = int(inp)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = input
        largest = input
    if input < smallest:
        smallest = input
    if input > largest:
        largest = input

print "Maximum is", largest
print "Minimum is", smallest
        