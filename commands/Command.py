from input_error import input_error
from addressbook import AddressBook

class Command:
    
    names = [] # override this field

    def execute(self, book: AddressBook, args) -> str:
        raise NotImplementedError("Command is not implemented yet")
    
    @input_error
    def safe_execute(self, book: AddressBook, args) -> str:
        return self.execute(book, args)