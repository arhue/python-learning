smallest=None
largest=None
while True:
    
    number=input("Enter number")
    
    if number=="done":
        break    

    try:
        number=int(number)
    except:
        print("Invalid input")
        continue

    if (smallest is None) or (largest is None):
        smallest=number
        largest=number
    elif number > largest:
        largest=number
    elif number < smallest:
        smallest=number

print("Maximum is", largest)
print("Minimum is", smallest)
