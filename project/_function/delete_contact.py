from _decorator.decorator import input_error_name
from _classes.adress_book import AddressBook


@input_error_name
def delete_contact(args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    del record
    return print(f"Contact {name} deleted.")