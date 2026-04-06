print("1. Sandwich")
print("2. Pizza")
print("3. Burger")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You ordered Sandwich")
    
    case 2:
        print("Select Pizza type:")
        print("1. Thin Crust")
        print("2. Cheese Burst")
        print("3. Fresh Dough")
        sub = int(input("Enter choice: "))
        
        match sub:
            case 1:
                print("Thin Crust Pizza ordered")
            case 2:
                print("Cheese Burst Pizza ordered")
            case 3:
                print("Fresh Dough Pizza ordered")
            case _:
                print("Invalid choice")

    case 3:
        print("You ordered Burger")
    
    case _:
        print("Invalid choice")