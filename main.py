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


def show_notes(notes):
    """Выводит список заметок с номерами."""
    if not notes:
        print("Заметок пока нет")
    for number, text in enumerate(notes, 1):
        print(f"{number}. {text}")


def main():
    notes = load_notes()
    while True:
        choice = input("1 — добавить, 2 — список, 0 — выход: ").strip()
        if choice == "1":
            try:
                add_note(notes, input("Текст заметки: "))
            except ValueError as error:
                print(error)
        elif choice == "2":
            show_notes(notes)
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
