x=input("Input no.: ")

try:
    x=int(x)
except:
    print("Please enter a proper number")
    quit()

def oddoreven(number):
    if number is 0:
        print("No is neither odd nor even")
    elif number%2 is 0:
        print("Number is even")
        if number%4 is 0:
            print("Number is also a multiple of 4")
    elif number%2 is 1:
        print("Number is odd")

oddoreven(x)

