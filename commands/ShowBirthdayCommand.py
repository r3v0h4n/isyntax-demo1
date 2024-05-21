from commands.Command import Command
from addressbook import AddressBook

class ShowBirthdayCommand(Command):

    names = ["show-birthday"]
    
    def execute(self, book: AddressBook, args) -> str:
        name = args[0]
        record = book.find(name, strict=True)
        return str(record.birthday)