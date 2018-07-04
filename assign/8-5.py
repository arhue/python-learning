file=open("mbox-short.txt","r")
y=list()
for i in file:
    if i.startswith("From:"): continue
    if i.startswith("From"):
        x=i.split()
        y.append(x[1])

for k in y:
    print(k)
print("There were",len(y),"lines in the file with From as the first word")
