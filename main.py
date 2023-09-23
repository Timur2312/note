import os

class NoteManager:
    def __init__(self, notes_directory):
        self.notes_directory = notes_directory
        self.create_notes_directory()

    def create_notes_directory(self):
        if not os.path.exists(self.notes_directory):
            os.mkdir(self.notes_directory)

    def create_note(self, note_title, note_content):
        note_path = os.path.join(self.notes_directory, f"{note_title}.txt")
        with open(note_path, "w") as note_file:
            note_file.write(note_content)

    def read_notes(self):
        notes_list = []
        for filename in os.listdir(self.notes_directory):
            if filename.endswith(".txt"):
                note_path = os.path.join(self.notes_directory, filename)
                with open(note_path, "r") as note_file:
                    note_content = note_file.read()
                    notes_list.append((filename[:-4], note_content))  # Убираем расширение ".txt"
        return notes_list

    def edit_note(self, note_title, new_note_content):
        note_path = os.path.join(self.notes_directory, f"{note_title}.txt")
        if os.path.exists(note_path):
            with open(note_path, "w") as note_file:
                note_file.write(new_note_content)
        else:
            print("Заметка не найдена.")

    def delete_note(self, note_title):
        note_path = os.path.join(self.notes_directory, f"{note_title}.txt")
        if os.path.exists(note_path):
            os.remove(note_path)
        else:
            print("Заметка не найдена.")

def main():
    notes_manager = NoteManager("notes_directory")

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            note_title = input("Введите название заметки: ")
            note_content = input("Введите текст заметки: ")
            notes_manager.create_note(note_title, note_content)
            print("Заметка создана успешно!")

        elif choice == "2":
            notes_list = notes_manager.read_notes()
            if notes_list:
                print("\nСписок заметок:")
                for i, (note_title, _) in enumerate(notes_list):
                    print(f"{i + 1}. {note_title}")
            else:
                print("Список заметок пуст.")

        elif choice == "3":
            note_title = input("Введите название заметки для редактирования: ")
            new_note_content = input("Введите новый текст заметки: ")
            notes_manager.edit_note(note_title, new_note_content)
            print("Заметка отредактирована успешно!")

        elif choice == "4":
            note_title = input("Введите название заметки для удаления: ")
            notes_manager.delete_note(note_title)
            print("Заметка удалена успешно!")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
