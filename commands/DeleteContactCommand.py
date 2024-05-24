'''module provides class for deletion contact from the book'''
from commands.Command import Command
from addressbook import AddressBook
from input_error import input_error

class DeleteContactCommand(Command):
    '''delete contact command class'''
    names = ["delete"]

    @input_error
    def execute(self, book: AddressBook, args) -> str:
        record = book.find(args[0] if len(args)>0 else None, strict=True)
        if record:
            book.delete(args[0])
            return "Record deleted."
        raise f"No records with this name: {args[0]}"
