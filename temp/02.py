from collections import UserDict
import re


class PhoneValidationError(ValueError):
    pass

class NameValidationError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args[0]
            
            if not re.match(r'^[a-zA-Zа-яА-Я]+$', name): 
                raise NameValidationError

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError
            
            return func(*args, **kwargs)
        
        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        # except KeyError:
        #     print ("Enter user name")
        # except ValueError:
        #     print ("Give me name and phone please")
        # except IndexError:
        #     print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name = name.lower()
        for key, record in self.data.items():
            if record.name.value.lower() == name:
                return record
        return None
    
    def delete(self, name):
        name_lower = name.lower()  
        for key, record in self.data.items():
            if record.name.value.lower() == name_lower:  
                del self.data[key]  
                return  
        raise ValueError("Record not found.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone_field = Phone(phone)
        phone_field.validate()
        self.phones.append(phone_field)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        if not self.value.strip():
            raise ValueError("Name cannot be empty.")

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        if not re.match(r'^\d{10}$', self.value):
            raise ValueError("Invalid phone number format. Phone number should contain 10 digits.")        

@input_error
def add_contact(args, book: 'AddressBook'):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        name_obj = Name(name)
        record = Record(name_obj)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

def parse_input(user_input): 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

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

 

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()






