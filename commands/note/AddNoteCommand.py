from commands.note.NoteCommand import NoteCommand

class AddNoteCommand(NoteCommand):
    names = ["add-note"]

    def execute(self, notes, args):
        # todo add after Notes class is implemented
        return notes