from commands.Command import Command
from addressbook import AddressBook

class AddEmailCommand(Command):
    ''' class for adding email'''
    names = ["add-email"]

    def execute(self, book: AddressBook, args) -> str:
        name, email = args
        record = book.find(name, strict=True)
        try:
            if record:
                record.add_email(email)
                return "Email added."
        except Exception as e:
            return e

