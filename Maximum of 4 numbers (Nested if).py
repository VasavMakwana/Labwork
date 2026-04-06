a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            print("Maximum is:", a)
        else:
            print("Maximum is:", d)
    else:
        if c > d:
            print("Maximum is:", c)
        else:
            print("Maximum is:", d)
else:
    if b > c:
        if b > d:
            print("Maximum is:", b)
        else:
            print("Maximum is:", d)
    else:
        if c > d:
            print("Maximum is:", c)
        else:
            print("Maximum is:", d)
            