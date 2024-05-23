from commands.Command import Command
from addressbook import AddressBook

class GetEmailCommand(Command):

    names = ["email"]
    
    def execute(self, book: AddressBook, args) -> str:
        name = args[0]
        record = book.find(name, strict=True)
        return ", ".join(str(email) for email in record.emails)