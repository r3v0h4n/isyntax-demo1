from commands.Command import Command
from addressbook import AddressBook

class GetPhoneCommand(Command):

    names = ["phone"]
    
    def execute(self, book: AddressBook, args) -> str:
        name = args[0]
        record = book.find(name, strict=True)
        return ", ".join(str(phone) for phone in record.phones)