from commands.note.NoteCommand import NoteCommand
from note import Note, Notebook

class SeachNoteCommand(NoteCommand):
    names = ["search-note"]

    def execute(self, notebook: Notebook, args) -> str:
        value = args[0]
        return "\n\n".join(str(note) for note in notebook.search(value))