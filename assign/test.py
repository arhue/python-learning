file=open("txt.txt","r")

for line in file:
    if not line.startswith("From"): continue
    x=line.split()
    print(x[2])
