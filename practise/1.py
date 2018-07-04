import datetime
now = datetime.datetime.now()
year=now.year
    

name=input("Enter your name: ")
age=input("Enter your age: ")

try:
    age=int(age)    
except:
    print("Please enter age properly.")
    quit()

q=0

for i in name:
    try:
        int(i)
        q=1
        break
    except:
        pass

if q is 1:
    print("No numbers in names")
    quit()

if age > 200 or len(name) > 100:
    print("Please check age/Name too long")
    quit()

print("Your name is: ", name)
print("Your DOB is: ", year-age)
