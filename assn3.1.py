hours = raw_input("Enter hours: ")
rate_per_hour = raw_input("Enter the rate per hour: ")
hrs = float(hours)
rph = float(rate_per_hour)
if hrs > 40 :
    gross_pay = 40 * rph + (hrs - 40) * rph * 1.5
else :
    gross_pay = hrs * rph
print gross_pay