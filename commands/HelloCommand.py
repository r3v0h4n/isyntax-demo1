from commands.Command import Command
from addressbook import AddressBook

class HelloCommand(Command):

    names = ["hello"]
    
    def execute(self, book: AddressBook, args) -> str:
        return "How can I help you?"