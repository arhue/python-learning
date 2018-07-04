hrs = input("Enter no. of hrs")
payrate = input("Enter the pay per hour")
hrs=float(hrs)
payrate=float(payrate)
if hrs > 40:
    pay=(40*payrate)+(1.5*(hrs-40)*payrate)
else:
    pay=hrs*payrate
print(pay)
