def menu():
    print("Menu \n 1. Celsius to Farenheit \n2. Farenheit to Celsius \n 3. Exit")

    try:
        choice = int(input("Enter your choice "))

    except ValueError as e:
        print(e)
        choice = 0

    return choice

if __name__ == '__main__':

    choice = menu()
    while choice != 3:
        if choice is 1:
            count = int(input("How many temperature conversions?"))
            for i in range(0,count):           # 2only
                Celsius = int(input("Enter a temperature in Celsius: "))
                Fahrenheit = 9.0 / 5.0 * Celsius + 32
                print("Temperature: Celsius", Celsius , "Fahrenheit: ", Fahrenheit)

        elif choice == 2:
            count = int(input("How many temperature conversions?"))
            for i in range(0, count):
                Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
                Celsius = Fahrenheit - 32 / 1.8000
                print("Temperature: Celsius", Celsius , "Fahrenheit: ", Fahrenheit)
        else:
            print("Try Again!!")

        choice = menu()

