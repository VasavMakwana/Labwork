#Maximum number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Maximum is:", a)
    else:
        print("Maximum is:", c)
else:
    if b > c:
        print("Maximum is:", b)
    else:
        print("Maximum is:", c)
        
#Minimum number
if a < b:
    if a < c:
        print("Minimum is:", a)
    else:
        print("Minimum is:", c)
else:
    if b < c:
        print("Minimum is:", b)
    else:
        print("Minimum is:", c)