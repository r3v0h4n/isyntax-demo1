from address import Address
from name import Name
from phone import Phone
from birthday import Birthday
from contact_email import Email

class Record:
    def __init__(self, name: str) -> None:
        self.__name = Name(name)
        self.__phones = []
        self.__birthday = None
        self.__address = None
        self.__emails = []

    def add_birthday(self, value: str):
        self.__birthday = Birthday(value)

    def add_phone(self, phone: str) -> None:
        self.__phones.append(Phone(phone))

    def add_address(self, address: str) -> None:
        self.__address = Address(address)

    def remove_phone(self, phone: str) -> None:
        self.__phones.remove(self.find_phone(phone))

    def find_phone(self, value: str) -> Phone:
        try:
            return next(phone for phone in self.__phones if phone.value == value)
        except StopIteration:
            raise ValueError(f"Contact {self.__name} doesn't have phone {value}!")
    
    def edit_phone(self, phone_to_edit: str, phone: str) -> None:
        self.find_phone(phone_to_edit).value = phone

    def add_email(self, email: str) -> None:
        self.__emails.append(Email(email))

    def find_email(self, value: str) -> Email:
        try:
            return next(email for email in self.__emails if email.value == value)
        except StopIteration:
            raise ValueError(f"Contact {self.__name} doesn't have email {value}!")

    def edit_email(self, email_to_edit: str, new_email: str) -> None:
        self.find_email(email_to_edit).value = new_email

    def __str__(self) -> str:
        return f"Contact name: {self.__name}, birthday: {self.__birthday}, address: {self.__address}, phones: {'; '.join(str(phone) for phone in self.__phones)}, emails: {'; '.join(str(email) for email in self.__emails)}"
    
    @property
    def name(self) -> Name:
        return self.__name
    
    @property
    def address(self) -> Address:
        return self.__address
    
    @property
    def birthday(self) -> Birthday:
        return self.__birthday
    
    @property
    def phones(self) -> list:
        return self.__phones

    @property
    def emails(self) -> list:
        return self.__emails