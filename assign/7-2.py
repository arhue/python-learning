while True:
    try:
        x=input("Enter filename:")
        file=open(x,"r")
        break
    except:
        print("Incorrect filename. Please enter correct filename. Enter \"done\" to quit")
        if x=="done":
            quit()

count=0
no=0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        char=line.find(":")
        val=line[char+1:]
        noval=float(val.strip())
        count=count+1
        no=no+noval

print("Average spam confidence:", no/count)
