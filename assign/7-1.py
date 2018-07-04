while True:
    try:
        x=input("Enter filename:")
        file=open(x,"r")
        break
    except:
        print("Incorrect filename. Please enter correct filename. Enter \"done\" to quit")
        if x=="done":
            quit()

y=file.read()
z=y.rstrip()
print(z.upper())
