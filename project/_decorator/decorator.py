import re
from datetime import datetime

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
        except KeyError:
            print ("Enter user name")
        except ValueError:
            print ("Give me name and phone please")
        except IndexError:
            print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner

def input_error_phones(func):
    def inner(*args, **kwargs):
        try:
            name, phone, new_phone, *_ = args[0]
            
            if not re.match(r'^[a-zA-Za-яА-Я]+$', name): 
                raise NameValidationError

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError
            
            if not re.match(r'^\d{10,}$', new_phone):
                raise PhoneValidationError
            
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
        # except KeyError:
        #     print ("Enter user name")
        # except ValueError:
        #     print ("Give me name please")
        # except IndexError:
        #     print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner

def input_error_birthday(func):
    def inner(*args, **kwargs):
        try:
            name, birthday = args[0]
            
            if not re.match(r'^[a-zA-Za-яА-Я]+$', name): 
                raise NameValidationError

            birthday_obj = datetime.strptime(birthday, '%d.%m.%Y')  # Перевірка та створення об'єкта дати
            current_year = datetime.now().year
            if birthday_obj.year < 1900 or birthday_obj.year > current_year:
                raise ValueError("Invalid year. Birth year should be between 1900 and current year.")
            
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