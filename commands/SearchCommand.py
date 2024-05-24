from commands.Command import Command
from addressbook import AddressBook

class SearchCommand(Command):

    names = ["search"]
    
    def execute(self, book: AddressBook, args) -> str:
        value = args[0]
        return "\n".join(str(record) for record in book.search(value))