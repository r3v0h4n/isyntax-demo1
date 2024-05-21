from addressbook import AddressBook
import pickle
from commands.HelloCommand import HelloCommand
from commands.AddContactCommand import AddContactCommand
from commands.GetPhoneCommand import GetPhoneCommand
from commands.ChangeContactCommand import ChangeContactCommand
from commands.AllCommand import AllCommand
from commands.AddBirthdayCommand import AddBirthdayCommand
from commands.ShowBirthdayCommand import ShowBirthdayCommand
from commands.BirthdaysCommand import BirthdaysCommand

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    
    book = load_data()
    commands = [HelloCommand(), AddContactCommand(), GetPhoneCommand(), ChangeContactCommand(), AllCommand(), AddBirthdayCommand(), ShowBirthdayCommand(), BirthdaysCommand()]

    while True:
        user_input = input("Enter a command: ")
        entered_command, *args = parse_input(user_input)

        if entered_command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        for command in commands:
            if entered_command in command.names:
                print(command.safe_execute(book, args))
                break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()