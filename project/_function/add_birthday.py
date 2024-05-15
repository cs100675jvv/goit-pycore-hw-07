from _decorator.decorator import input_error_birthday
from _classes.adress_book import AddressBook
# from _classes.record import Record


@input_error_birthday
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birth(birthday)
    return print(f"Birthday for contact {name} updated.")