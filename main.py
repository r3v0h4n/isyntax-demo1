from addressbook import AddressBook
import pickle
from commands.Command import Command
from commands.HelloCommand import HelloCommand
from commands.AddContactCommand import AddContactCommand
from commands.GetPhoneCommand import GetPhoneCommand
from commands.ChangeContactCommand import ChangeContactCommand
from commands.AllCommand import AllCommand
from commands.AddBirthdayCommand import AddBirthdayCommand
from commands.ShowBirthdayCommand import ShowBirthdayCommand
from commands.BirthdaysCommand import BirthdaysCommand
from commands.AddAddressCommand import AddAddressCommand
from commands.AddEmailCommand import AddEmailCommand
from commands.GetEmailCommand import GetEmailCommand
from commands.note.NoteCommand import NoteCommand
from commands.note.AddNoteCommand import AddNoteCommand
from commands.note.UpdateNoteCommand import UpdateNoteCommand
from note import Notebook

def save_data(object, filename):
    with open(filename, "wb") as f:
        pickle.dump(object, f)

def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book_filename = "addressbook.pkl"
    notes_filename = "notes.pkl"
    book = load_data(book_filename) or AddressBook()
    notes = load_data(notes_filename) or Notebook()
    
    commands: list[Command] =\
    [
        HelloCommand(),
        AddContactCommand(),
        GetPhoneCommand(),
        ChangeContactCommand(),
        AllCommand(),
        AddBirthdayCommand(),
        ShowBirthdayCommand(),
        BirthdaysCommand(),
        GetEmailCommand(),
        AddAddressCommand(),
        AddEmailCommand(),
        AddNoteCommand(),
        UpdateNoteCommand()
    ]

    while True:
        user_input = input("Enter a command: ")
        entered_command, *args = parse_input(user_input)

        if entered_command in ["close", "exit"]:
            save_data(book, book_filename)
            save_data(notes, notes_filename)            
            print("Good bye!")
            break

        for command in commands:
            if entered_command in command.names:
                if isinstance(command, NoteCommand): 
                    print(command.safe_execute(notes, args))
                else:
                    print(command.safe_execute(book, args))
                break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
