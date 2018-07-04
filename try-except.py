x=input("Enter a no. I will convert to integer")
z=1
try:
    y=int(float(x))
    z="float"
except:
    z="wrong"

if z=="wrong":
    print("fix your input")
else:    
    print("int of your input is:", y)
