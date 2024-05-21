from commands.Command import Command
from addressbook import AddressBook

class BirthdaysCommand(Command):

    names = ["birthdays"]    
    
    def __format_upcoming_birthday(self, record, congratulation_date) -> str:
        return f"Contact: {record.name}, congratulation date: {congratulation_date.strftime('%d.%m.%Y')}"

    def execute(self, book: AddressBook, args) -> str:
        return "\n".join(self.__format_upcoming_birthday(*item) for item in book.get_upcoming_birthdays())