from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    def __init__(self, name: str) -> None:
        self.__name = Name(name)
        self.__phones = []
        self.__birthday = None

    def add_birthday(self, value: str):
        self.__birthday = Birthday(value)

    def add_phone(self, phone: str) -> None:
        self.__phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.__phones.remove(self.find_phone(phone))

    def find_phone(self, value: str) -> Phone:
        try:
            return next(phone for phone in self.__phones if phone.value == value)
        except StopIteration:
            raise ValueError(f"Contact {self.__name} doesn't have phone {value}!")
    
    def edit_phone(self, phone_to_edit: str, phone: str) -> None:
        self.find_phone(phone_to_edit).value = phone

    def __str__(self) -> str:
        return f"Contact name: {self.__name}, birthday: {self.__birthday}, phones: {'; '.join(str(phone) for phone in self.__phones)}"
    
    @property
    def name(self) -> Name:
        return self.__name
    
    @property
    def birthday(self) -> Birthday:
        return self.__birthday
    
    @property
    def phones(self) -> list:
        return self.__phones
