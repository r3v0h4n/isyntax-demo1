from commands.Command import Command
from record import Record
from addressbook import AddressBook

class AddContactCommand(Command):

    names = ["add"]
    
    def execute(self, book: AddressBook, args) -> str:
        name, phone = args    
        record = book.find(name)
        message = "Contact updated."
        if not record:
            record = Record(name)
            book.add_record(record)
            message = "Contact added."
        record.add_phone(phone)
        return message