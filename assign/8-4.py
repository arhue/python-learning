file=open("romeo.txt","r")
x=list()
for i in file:
    for j in i.split():
        if j in x: continue
        x.append(j)
x.sort()
print(x)
