from commands.note.NoteCommand import NoteCommand
from note import Note

class AddNoteCommand(NoteCommand):
    names = ["add-note"]

    def execute(self, notebook, args):
        title = args[0]
        body = args[1]
        tags = []
        if len(args) > 2:
            tags = args[2:]
        
        notebook.add(Note(title, body, tags))
        return "Note added."