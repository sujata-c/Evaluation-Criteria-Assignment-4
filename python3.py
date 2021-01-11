def menu():
    print "Menu \n 1. Celsius to Farenheit \n2. Farenheit to Celsius \n 3. Exit"

    try:
        choice = int(raw_input("Enter your choice "))  # 2only

    except ValueError, e:  #2only
        print e             # 2only
        choice = 0

    return choice
# xrange
# string unicode
# Python 2 only
# class Upper(object):

if __name__ == '__main__':

    choice = menu()
    while choice != 3:
        if choice is 1:
            count = int(raw_input("How many temperature conversions?"))
            for i in xrange(0,count):           # 2only
                Celsius = int(raw_input("Enter a temperature in Celsius: "))
                Fahrenheit = 9.0 / 5.0 * Celsius + 32
                print "Temperature: Celsius", Celsius , "Fahrenheit: ", Fahrenheit

        elif choice == 2:
            count = int(raw_input("How many temperature conversions?"))
            for i in xrange(0, count):
                Fahrenheit = int(raw_input("Enter a temperature in Fahrenheit: "))
                Celsius = Fahrenheit - 32 / 1.8000
                print "Temperature: Celsius", Celsius , "Fahrenheit: ", Fahrenheit
        else:
            print "Try Again!!"

        choice = menu()

