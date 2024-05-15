from _classes.fields import Name, Phone, Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone_field = Phone(phone)
        # phone_field.validate()
        self.phones.append(phone_field)

    def delete_phone(self, phone):
        for i, phone_field in enumerate(self.phones):
            if phone_field.value == phone:
                del self.phones[i]
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, phone, new_phone):
        for phone_field in self.phones:
            if phone_field.value == phone:
                phone_field.value = new_phone
                # phone_field.validate()
                return
        raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for phone_field in self.phones:
            if phone_field.value == phone:
                return phone
        raise ValueError("Phone number not found.")
    
    def add_birth(self, birthday):
        birthday_obj = Birthday(birthday)
        self.birthday = birthday_obj
        return 
    
    # def show_birth(self, birthday):
    #     birthday_obj = Birthday(birthday)
    #     # self.birthday = birthday_obj
    #     return birthday_obj
    

    def __str__(self):
        birthday_info = f", Birthday: {self.birthday.value.strftime('%d-%m-%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}{birthday_info}"