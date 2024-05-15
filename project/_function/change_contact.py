from _decorator.decorator import input_error_phones
from _classes.adress_book import AddressBook


@input_error_phones
def change_contact(args, book: 'AddressBook'):
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(phone, new_phone)
        return print(f"Contact {name} now has phone: {new_phone}")
    else:
        return print(f"Contact {name} not found in our dictionary.")