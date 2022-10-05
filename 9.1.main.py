convert_rate = float(0.621371)

print("Hello! In this program, you can convert kilometers to miles.\r\n")

while True:
    var_km = float(input("Enter the number of kilometers that you need to convert: "))
    var_mil = var_km * convert_rate
    print(f"This is exactly {var_mil} miles.\r\n")

    another = input(str(f"Would you like to convert another number? Type YES or NO: "))
    if another.lower() != "yes":
        print("Have a nice trip, goodbye")
        break
