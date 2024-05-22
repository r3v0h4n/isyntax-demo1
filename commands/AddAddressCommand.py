from commands.Command import Command
from record import Record
from addressbook import AddressBook

class AddAddressCommand(Command):

    names = ["add-address"]
    
    def execute(self, book: AddressBook, args) -> str:
        name, address = args    
        record = book.find(name)
        message = "Address updated."
        if not record:
            record = Record(name)
            book.add_record(record)
            message = "Address added."
        record.add_address(address)
        return message