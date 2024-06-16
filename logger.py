from notes_create import title_data, body_data, id_data, save_notes, notes
import datetime

def add_note():
    title = title_data()
    body = body_data()
    note_id = id_data()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "body": body, "date": date})
    save_notes()
    print("Заметка успешно сохранена")

def read_notes():
    filter_date = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    if not notes:
        print("Заметок нет")
        return
    if not filter_date:
        for note in notes:
            print(f"{note['id']}; {note['title']}; {note['body']}; ({note['date']})\n")
    else:
        filtered_notes = [note for note in notes if note["date"].startswith(filter_date)]
        if filtered_notes:
            for note in filtered_notes:
                print(f"{note['id']}; {note['title']}; {note['body']}; ({note['date']})\n")
        else:
            print("Заметок с указанной датой нет")

def edit_note():
    note_id = input("Введите id заметки для редактирования: ")
    for note in notes:
        if note["id"] == note_id:
            title = input(f"Введите новый заголовок заметки ({note['title']}): ")
            body = input(f"Введите новое содержание заметки ({note['body']}): ")
            if title:
                note["title"] = title
            if body:
                note["body"] = body
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована")
            return
    print(f"Заметка с id {note_id} не найдена")

def read_note_by_id():
    note_id = input("Введите ID заметки, которую хотите прочитать: ")
    for note in notes:
        if note["id"] == note_id:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']} ({note['date']})\nСодержимое: {note['body']}")
            return
    print(f"Заметка с ID {note_id} не найдена")

def delete_note():
    note_id = input("Введите id заметки для удаления: ")
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена")
            return
    print(f"Заметка с id {note_id} не найдена")

