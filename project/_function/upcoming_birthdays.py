from datetime import datetime, timedelta


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