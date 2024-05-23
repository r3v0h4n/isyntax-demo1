from commands.note.NoteCommand import NoteCommand
from note import Note

class UpdateNoteCommand(NoteCommand):
    names = ["update-note", "change-note"]

    def execute(self, notebook, args):
        title = args[0]
        body = args[1]
        tags = []
        if len(args) > 2:
            tags = args[2:]

        note = notebook.find(title)
        if not note:
            raise ValueError("Note not found!")
        
        note.body = body
        for tag in tags:
            note.add_tag(tag)

        return "Note updated."