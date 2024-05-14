from collections import UserDict
from datetime import datetime, timedelta
import re


class PhoneValidationError(ValueError):
    pass

class NameValidationError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args[0]
            
            if not re.match(r'^[a-zA-Za-яА-Я]+$', name): 
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

def input_error_name(func):
    def inner(*args, **kwargs):
        try:
            name, = args[0]
            
            if not re.match(r'^[a-zA-Za-яА-Я]+$', name): 
                raise NameValidationError
            
            return func(*args, **kwargs)
        
        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print ("Enter user name")
        except ValueError:
            print ("Give me name and phone please")
        except IndexError:
            print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner




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

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def validate(self):
        current_year = datetime.now().year
        if self.value.year < 1900 or self.value.year > current_year:
            raise ValueError("Invalid year. Birth year should be between 1900 and current year.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone_field = Phone(phone)
        phone_field.validate()
        self.phones.append(phone_field)

    def delete_phone(self, phone):
        for i, phone_field in enumerate(self.phones):
            if phone_field.value == phone:
                del self.phones[i]
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        for phone_field in self.phones:
            if phone_field.value == old_phone:
                phone_field.value = new_phone
                phone_field.validate()
                return
        raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for phone_field in self.phones:
            if phone_field.value == phone:
                return phone
        raise ValueError("Phone number not found.")
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        self.birthday.validate()


    @input_error
    def add_birthday(args, book):
        pass
        # реалізація

    @input_error
    def show_birthday(args, book):
        pass
        # реалізація

    @input_error
    def birthdays(args, book):
        pass
        # реалізація

    def __str__(self):
        birthday_info = f", Birthday: {self.birthday.value.strftime('%d-%m-%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}{birthday_info}"

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


def get_upcoming_birthdays(book):
    today = datetime.today().date()  
    upcoming_birthdays = []  

    for record in book.data.values():  
        if record.birthday:  
            user_birthday = record.birthday.value.date()  
            birthday_this_year = user_birthday.replace(year=today.year) 
            if birthday_this_year < today:  
                birthday_this_year = user_birthday.replace(year=today.year + 1)
            day_delta = (birthday_this_year - today).days  

            if 0 <= day_delta <= 7:  
                if birthday_this_year.weekday() == 5:  
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:  
                    birthday_this_year += timedelta(days=1)

                upcoming_birthdays.append({  
                    'name': record.name.value,
                    'congratulation_date': birthday_this_year.strftime('%Y-%m-%d')
                })
    return upcoming_birthdays

def parse_input(user_input): 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return print(message)



@input_error
def change_contact(args, book: 'AddressBook'):
    name, phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        return print(f"Contact {name} now has phone: {new_phone}")
    else:
        return print(f"Contact {name} not found in our dictionary.")

@input_error_name
def delete_contact(args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    del record
    return print(f"Contact {name} deleted.")

@input_error_name
def show_phone (args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    if record:
        return print(f"Contact {name} has phone: {'; '.join(str(p) for p in record.phones)}")
    else:
        return print(f"Contact {name} not found in our dictionary.")


def show_all (book):
    for name, phone in book.items():
        print(f"{name}: {phone}")




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

        # elif command == "show-birthday":
        #     # реалізація

        # elif command == "birthdays":
        #     # реалізація


        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()






