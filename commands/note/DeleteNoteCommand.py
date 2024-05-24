from commands.note.NoteCommand import NoteCommand
from note import Note

class DeleteNoteCommand(NoteCommand):
    names = ["delete-note", "del-note", "remove-note", "rem-note"]

    def execute(self, notebook, args):
   
        title = args[0]
        note = notebook.find(title)
        if not note:
            raise ValueError(f"Note with title: '{title}' is not found.")
        notebook.remove(title)
        return f"Note titled '{title}' has been removed."
