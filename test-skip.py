test=open("mbox.txt","r")
for i in test:
    x=i.rstrip()
    if "a" in i:
        print(x)
