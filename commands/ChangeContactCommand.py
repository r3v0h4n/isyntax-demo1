from commands.Command import Command
from addressbook import AddressBook

class ChangeContactCommand(Command):

    names = ["change"]
    
    def execute(self, book: AddressBook, args) -> str:
        name, phone_to_edit, phone = args
        record = book.find(name, strict=True)
        record.edit_phone(phone_to_edit, phone)

        return "Contact changed."