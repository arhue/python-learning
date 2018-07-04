def thing(y):
    try:
        x=float(y)
    except:
        print("enter a valid no.")
        quit()
    return x*10

number=input("enter no. to be multiplied by 10")

y=1

print(thing(number))
print(y)
