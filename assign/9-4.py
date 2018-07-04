file=open("mbox-short.txt","r")
mail=dict()
words=list()
for line in file:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        words=line.split()
        if len(words)<7:
            continue
        else:
            mail[words[1]]=mail.get(words[1],0)+1

maxmail=None
maxtimes=None
for mail,times in mail.items():
    if maxtimes is None or times>maxtimes:
        maxmail=mail
        maxtimes=times

print(maxmail,maxtimes)
