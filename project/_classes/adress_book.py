from collections import UserDict

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