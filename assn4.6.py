hours = raw_input("Enter hours: ")
rate_per_hour = raw_input("Enter rate per hour: ")

hrs = float(hours)
rph = float(rate_per_hour)

def computepay(h,r):
    if h > 40:
        gp = 40 * r + (h - 40) * r * 1.5
    else:
        gp = h * r
    return gp

print computepay(hrs,rph)
        