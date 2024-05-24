from commands.note.NoteCommand import NoteCommand
from note import Note

class AddNoteCommand(NoteCommand):
    names = ["add-note"]

    def execute(self, notebook, args):
        title = args[0]
        body = " ".join(args[1:])
        
        notebook.add(Note(title, body))
        return "Note added."