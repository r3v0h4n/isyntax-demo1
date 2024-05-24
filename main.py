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
from commands.SearchCommand import SearchCommand
from commands.note.NoteCommand import NoteCommand
from commands.note.AddNoteCommand import AddNoteCommand
from commands.note.UpdateNoteCommand import UpdateNoteCommand
from commands.note.SeachNoteCommand import SeachNoteCommand
from note import Notebook

from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

from commands.DeleteContactCommand import DeleteContactCommand

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

def get_commands_dict(commands):
    # create 1 list from list of lists
    command_names = []
    for command in commands:
        command_names.extend(command.names)

    command_names.extend(["close", "exit"])

    # autocompleter requires dict, because otherwise autocompletion will occur on every word
    return {command: None for command in command_names}


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
        UpdateNoteCommand(),
        SearchCommand(),
        SeachNoteCommand(),
        DeleteContactCommand()

    ]

    completer = NestedCompleter.from_nested_dict(get_commands_dict(commands))

    while True:
        user_input = prompt('Enter a command: ', completer=completer)
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
