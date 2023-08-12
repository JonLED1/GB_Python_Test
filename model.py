import datetime

class NoteBook:

    def __init__(self, path: str = 'c:/Git/GB_Python_Test/notes.txt'):
        self._note_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        file.close()
        self._note_book: list[dict[str, str]] = []
        for notes in data:
            note = notes.strip().split(';')
            new = {'id': note[0], 'data': note[1], 'text': note[2]}
            self._note_book.append(new)
        self._last_id = int(self._note_book[-1]['id'])

    def save(self):
        data = []
        for notes in self._note_book:
            data.append(';'.join([value for value in notes.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)
        file.close()

    def load(self):
        return self._note_book
    
    def add(self, note):
        self._last_id += 1
        new = {}
        new['id'] = str(self._last_id)
        new['data'] = (datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S"))
        new['text'] = note
        self._note_book.append(new)
        return new.get('id')
    
    def change(self, index, note):
        self._note_book[index]['text']=note
        
    def delete(self, index):
        self._note_book.pop(index)
    