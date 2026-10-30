"""Консольное приложение для ведения заметок."""
import json
from pathlib import Path

DATA_FILE = Path("notes.json")


def load_notes():
    """Загружает заметки из файла; если файла нет, возвращает пустой список."""
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_notes(notes):
    """Сохраняет заметки в JSON-файл."""
    DATA_FILE.write_text(json.dumps(notes, ensure_ascii=False, indent=2),
                         encoding="utf-8")


def add_note(notes, text):
    """Добавляет заметку, если текст не пустой."""
    text = text.strip()
    if not text:
        raise ValueError("Заметка не может быть пустой")
    notes.append(text)
    save_notes(notes)


def delete_note(notes, number):
    """Удаляет заметку по номеру (нумерация с 1)."""
    if not 1 <= number <= len(notes):
        raise ValueError("Заметки с таким номером нет")
    removed = notes.pop(number - 1)
    save_notes(notes)
    return removed


def search_notes(notes, query):
    """Возвращает заметки, содержащие строку query (без учёта регистра)."""
    query = query.lower()
    return [text for text in notes if query in text.lower()]


def show_notes(notes):
    """Выводит список заметок с номерами."""
    if not notes:
        print("Заметок пока нет")
    for number, text in enumerate(notes, 1):
        print(f"{number}. {text}")


MENU = "1 — добавить, 2 — список, 3 — удалить, 4 — поиск, 0 — выход: "


def main():
    notes = load_notes()
    while True:
        choice = input(MENU).strip()
        try:
            if choice == "1":
                add_note(notes, input("Текст заметки: "))
            elif choice == "2":
                show_notes(notes)
            elif choice == "3":
                removed = delete_note(notes, int(input("Номер: ")))
                print(f"Удалено: {removed}")
            elif choice == "4":
                show_notes(search_notes(notes, input("Найти: ")))
            elif choice == "0":
                break
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
