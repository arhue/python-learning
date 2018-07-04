a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=list()
number2=int(input("Enter number"))

for number in a:
    if number < number2:
        print(number)
        b.append(number)

print(b)
