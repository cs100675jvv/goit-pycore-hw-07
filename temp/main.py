from parse import parse_input
from add import add_contact
from change import change_contact
from delete import delete_contact
from show import show_phone, show_all

'''
Bot accepts commands:
    add <username phone> - for adding user with phone to dictionary
    change <username phone> - for changing user's phone
    delete <username> - for deleting user from dictionary
    show <username> - to show user's name and phone
    all - to show all user's names and phones
    close or exit - exit from bot
'''




def main():
    contacts = dict()
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
            add_contact(args, contacts)

        elif command == "delete":
            delete_contact(args, contacts)

        elif command == "show":
            show_phone(args, contacts)

        elif command == "change":
            change_contact(args, contacts)

        elif command == "phone":
            show_phone (args, contacts)

        elif command == "all":
            show_all(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
