from commands.Command import Command
from addressbook import AddressBook

class BirthdaysCommand(Command):

    names = ["birthdays"]
    in_next_days:int

    def __format_upcoming_birthday(self, record, congratulation_date) -> str:
        return f"Contact: {record.name}, congratulation date: {congratulation_date.strftime('%d.%m.%Y')}"

    def execute(self, book: AddressBook, args) -> str:
        self.in_next_days = int(args[0]) if len(args)>0 else 7
        return "\n".join(self.__format_upcoming_birthday(*item) for item in book.get_upcoming_birthdays(self.in_next_days))