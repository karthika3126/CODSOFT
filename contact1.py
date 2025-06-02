contacts = { }

def menu():
    print("--------------------MENU----------------------")
    print("press 4 if you want to terminate program.")
    print("press 0 to look up an existing number.")
    print("press 1 to add a Person to the contact book.")
    print("press 2 to update an existing number")
    print("press 3 to delete an existing number")
    print("press 5 to print all contacts")
    print("press any number from 6-9 to display Menu")
    print("----------------------------------------------")
    print("           DIGITAL CONTACT BOOK              ")
menu()
def display():
    for key, value1 in contacts.items():
        print(key, ":", value1)

while True:
    choice = int(input("Enter command:"))

    if choice == 0:
        look = input("Name of number owner:").upper()
        keys = list(contacts.keys())
        values1 = list(contacts.values())

        print("Number of ", look, ":", values1[keys.index(look)])
    elif choice == 1:
        Name = input("Name of new contact: ").upper()
        Number = input("Enter 11 or 8 digit number: ")
        if len(Number) == 11:
            contacts.update({Name: [Number, "Mobile"]})
            print("              CONTACTS")
            display()

        elif len(Number) == 8:
            contacts.update({Name:[Number, "Landline"]})
            print("              CONTACTS")
            display()
        else:
            print("Number is invalid.Please try again.")

    elif choice == 2:
        Name = input("Name of person to update contact:").upper()
        Number = input("New contact number( 11 or 8 digits):")
        if len(Number) == 11:
            contacts[Name] = [Number, "Mobile"]
            print("              CONTACTS")
            display()

        elif len(Number) == 8:
            contacts[Name] = [Number, "Landline"]
            print("              CONTACTS")
            display()
        else:
            print("Number is invalid.Please try again.")

    elif choice == 3:
        delete = input("Name of contact to remove:").upper()
        del contacts[delete]
        print("              CONTACTS")
        display()
    elif choice == 4:
        print("Thank you for using the Digital Contact Book!")
        break
    elif choice == 5:
        print("              CONTACTS")
        display()
    else:
        menu()
