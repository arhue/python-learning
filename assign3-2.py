hrs = input("Enter no. of hrs")
payrate = input("Enter the pay per hour")

try:
    hrs=float(hrs)
    payrate=float(payrate)
except:
    print("Please enter numbers")
    quit()

if hrs < 0 or payrate < 0:
    print("pay/hrs can't be -ve")
    quit()

if hrs > 40:
    print((40*payrate)+(1.5*(hrs-40)*payrate))
else:
    print(hrs*payrate)
