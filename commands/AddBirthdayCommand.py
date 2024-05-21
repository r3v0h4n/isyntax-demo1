from commands.Command import Command
from addressbook import AddressBook

class AddBirthdayCommand(Command):

    names = ["add-birthday"]
    
    def execute(self, book: AddressBook, args) -> str:
        name, birthday = args  
        record = book.find(name, strict=True)
        record.add_birthday(birthday)
        return "Birthday added."