from commands.Command import Command
from addressbook import AddressBook

class AllCommand(Command):

    names = ["all"]
    
    def execute(self, book: AddressBook, args) -> str:
        return "\n".join(str(record) for record in book.data.values())