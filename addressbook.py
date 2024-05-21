from collections import UserDict
from record import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        key = str(record.name)
        if key in self.data:
            raise ValueError("Contact with this name already exists!")
        
        self.data[key] = record

    def find(self, name: str, strict: bool = False) -> Record:
        record = self.data.get(name)
        if strict and not record:
            raise ValueError("Contact with this name does not exist!")
        return record
    
    def delete(self, name: str) -> None:
        del self.data[name]

    def get_upcoming_birthdays(self) -> list:
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()
            congratulation_date = birthday.replace(year=today.year)
            # Determine the date of the next birthday
            if congratulation_date < today:
                # If the birthday has already passed this year, consider next year
                congratulation_date = congratulation_date.replace(year=today.year + 1)

            # Calculate the difference between the birthday and today
            days_until_birthday = (congratulation_date - today).days

            # Check if the birthday falls within the next 7 days
            if days_until_birthday > 7:
                continue

            # Move the congratulation date to the next Monday if the birthday falls on a weekend
            weekday = congratulation_date.weekday()
            if weekday >= 5:
                congratulation_date += timedelta(days=7 - weekday)
            
            upcoming_birthdays.append((record, congratulation_date))

        return upcoming_birthdays
    