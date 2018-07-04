score=input("Enter the score between 0.0 and 1.0")

try:
    score=float(score)
except:
    print("Please enter numbers")
    quit()    

if (score < 0) or (score > 1):
    print("Invalid input. Score out of range")
elif score >=0.9:
    print("A")
elif score >=0.8:
    print("B")
elif score >=0.7:
    print("C")
elif score >=0.6:
    print("D")
else:
    print("F")
