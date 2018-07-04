x=None
for i in [2,643,-10,234235,23,234235465,3223,1]:
    if x == None:
        x=i
    elif i<x:
        x=i
print(x)
