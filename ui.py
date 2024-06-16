from logger import add_note, read_notes, read_note_by_id, edit_note, delete_note
def interface():
    print("Доброго времени суток! Перед вами приложение Заметки! \nВведите команду:\n1. Добавить \n 2. Прочитать \n 3. Редактировать \n 4. Удалить \n 5. Прочитать по ID \n 6. Выход \n")
    while True:
        command = int(input("Введите число: "))
        if command == 1:
            add_note()
        elif command == 2:
            read_notes()
        elif command == 3:
            edit_note()
        elif command == 4:
            delete_note()
        elif command == 5:
            read_note_by_id()
        elif command == 6:
            break
        else:
            print("Неверная команда")
