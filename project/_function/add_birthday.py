from _decorator.decorator import input_error_birthday
from _classes.adress_book import AddressBook
from _classes.record import Record


@input_error_birthday
def add_birthday(args, book: AddressBook):
    # self.birthday = Birthday(birthday)
    # self.birthday.validate()

    name, birthday, *_ = args
    birthday_obj = Birthday(birthday)
    record = book.find(name)
    record.add_birthday(birthday_obj)
    return print(f"Birthday for contact {name} updated.")