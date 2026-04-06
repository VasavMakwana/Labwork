print("Select Language:")
print("1. English")
print("2. Hindi")
print("3. Gujarati")

lang = int(input("Enter choice: "))

match lang:
    case 1:
        print("English Menu:")
        print("1. Balance Check")
        print("2. Recharge")
        sub = int(input("Enter choice: "))
        
        match sub:
            case 1:
                print("Your balance is Rs.100")
            case 2:
                print("Recharge successful")
            case _:
                print("Invalid option")

    case 2:
        print("Hindi Menu:")
        print("1. बैलेंस चेक")
        print("2. रिचार्ज")
        sub = int(input("Enter choice: "))
        
        match sub:
            case 1:
                print("आपका बैलेंस Rs.100 है")
            case 2:
                print("रिचार्ज सफल हुआ")
            case _:
                print("अमान्य विकल्प")

    case 3:
        print("Gujarati Menu:")
        print("1. બેલેન્સ ચેક")
        print("2. રિચાર્જ")
        sub = int(input("Enter choice: "))
        
        match sub:
            case 1:
                print("તમારું બેલેન્સ Rs.100 છે")
            case 2:
                print("રિચાર્જ સફળ થયું")
            case _:
                print("અમાન્ય વિકલ્પ")

    case _:
        print("Invalid language choice")