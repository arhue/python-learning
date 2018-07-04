numlist=list()
while True:
    x=input("Enter a no.")
    if x=="done": break
    x=float(x)
    numlist.append(x)
    
print(sum(numlist)/len(numlist))
