# Task 10: Phone Book Application

phone_book = {}

while True:
    command = input("Command (1 search, 2 add, 3 quit): ")

    if command == "1":
        name = input("Name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("No number found for", name)

    elif command == "2":
        name = input("Name: ")
        number = input("Number: ")
        phone_book[name] = number
        print("Ok!")

    elif command == "3":
        print("Quitting...")
        break
