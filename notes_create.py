import uuid
import json

def title_data():
    title = input("Введите название заголовка: ")
    return title

def body_data():
    body = input("Введите содерджимое заметки: ")
    return body

def id_data():
    note_id = str(uuid.uuid4())[0 : 3]
    return note_id

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
notes = load_notes()

   

