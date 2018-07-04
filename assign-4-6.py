hrs=input("Enter no. of hours worked")
rate=input("Enter pay rate")

try:
    hrs=float(hrs)
    rate=float(rate)
except:
    print("Please enter numbers")
    quit()

def pay(hrs,rate):
    if (hrs>40) and (rate>0):
        return 1.5*(hrs-40)*rate+40*rate
    elif (hrs>=0) and (rate>0):
        return hrs*rate
    else:
        print("Please enter valid numbers")
        quit()

print(pay(hrs,rate))
