'''Implement class Note, Notes'''

from collections import UserDict

class Note:
    def __init__(self, title: str, content: str, tags: list = None):
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError("Title must not be empty.")
        self.__title = value

    @property
    def content(self):
        return self.__note

    @content.setter
    def content(self, value: str):
        if not value:
            raise ValueError("Note content must not be empty.")
        self.__note = value

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, value: list):
        self.__tags = value

    def add_tag(self, tag: str):
        if not tag:
            raise ValueError("Tag must not be empty.")
        if tag not in self.__tags:
            self.__tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.__tags:
            self.__tags.remove(tag)

    def has_tag(self, tag: str) -> bool:
        return tag in self.__tags

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTags: {', '.join(self.tags)}"

class Notebook(UserDict):
    def add(self, note: Note):
        self.data[note.title] = note

    def find(self, title: str) -> Note:
        return self.data.get(title, None)

    def remove(self, title: str):
        if title in self.data:
            del self.data[title]

    def search(self, tag: str) -> list:
        result = [note for note in self.data.values() if note.has_tag(tag)]
        return result if result else None

# Example usage
if __name__ == "__main__":
    notebook = Notebook()
    
    note1 = Note("Shopping list", "Buy milk and eggs", ["shopping", "grocery"])
    note2 = Note("Homework", "Math exercises page 42", ["homework", "math"])
    note3 = Note("Meeting notes", "Discuss project milestones", ["meeting", "work"])

    notebook.add(note1)
    notebook.add(note2)
    notebook.add(note3)

    print("Find 'Homework' note:")
    found_note = notebook.find("Homework")
    if found_note:
        print(found_note)
    else:
        print("Note not found")

    print("\nRemove 'Shopping list' note:")
    notebook.remove("Shopping list")
    print(f"Remaining notes: {[note.title for note in notebook.values()]}")

    print("\nSearch for notes with tag 'work':")
    found_notes = notebook.search("work")
    if found_notes:
        for note in found_notes:
            print(note)
    else:
        print("No notes found with the given tag")
