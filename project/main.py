from _classes.adress_book import AddressBook
from _function.parse import parse_input
from _function.add_contact import add_contact
from _function.add_birthday import add_birthday
from _function.change_contact import change_contact
from _function.delete_contact import delete_contact
from _function.show import show_phone, show_all, show_birthday, birthdays



def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(args, book)

        elif command == "delete":
            delete_contact(args, book)

        elif command == "show":
            show_phone(args, book)

        elif command == "change":
            change_contact(args, book)

        elif command == "phone":
            show_phone (args, book)

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":
            add_birthday(args, book)

        elif command == "show-birthday":
            show_birthday(args, book)

        elif command == "birthdays":
            birthdays(book)

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()
