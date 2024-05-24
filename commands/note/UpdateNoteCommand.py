from commands.note.NoteCommand import NoteCommand
from note import Note

class UpdateNoteCommand(NoteCommand):
    names = ["update-note", "change-note"]

    def execute(self, notebook, args):
        title = args[0]
        content = " ".join(args[1:])

        note = notebook.find(title)
        if not note:
            raise ValueError("Note not found!")
        
        note.content = content
        return "Note updated."