x=open("test.txt","r")
x=x.read()
z=dict()
x=x.split()

for word in x:
    z[word]=1+z.get(word,0)    

print(z)

bigcount=None
bigword=None
count=0

for word,count in z.items():

    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
