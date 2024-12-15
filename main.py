from collections import UserDict
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту (обов'язкове поле)."""
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім.")
        super().__init__(value)


class Phone(Field):
    """Клас для зберігання номера телефону з валідацією формату (10 цифр)."""
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Номер телефону повинен містити рівно 10 цифр.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return bool(re.fullmatch(r"\d{10}", value))


class Birthday(Field):
    """Клас для зберігання дати народження у форматі DD.MM.YYYY."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я, телефони і день народження."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            print(f"Телефон {phone_number} не знайдено у записі {self.name}.")

    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            if Phone.validate(new_number):
                phone.value = new_number
            else:
                raise ValueError("Новий номер телефону повинен містити рівно 10 цифр.")
        else:
            print(f"Телефон {old_number} не знайдено у записі {self.name}.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = '; '.join(phone.value for phone in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"


class AddressBook(UserDict):
    """Клас для зберігання та управління записами у книзі контактів."""
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Запис з ім'ям {name} не знайдено.")

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today()
        for record in self.data.values():
            if record.birthday:
                # Перевіряємо, чи день народження буде на наступному тижні
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= today + timedelta(days=7):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays


def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            return str(e)
    return wrapper


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        raise ValueError(f"Contact {name} not found.")
    record.add_birthday(birthday)
    return f"Birthday for {name} added."


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if not record or not record.birthday:
        raise ValueError(f"Birthday for {name} not found.")
    return f"{name}'s birthday is {record.birthday}."


@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    return "\n".join([f"{record.name.value}: {record.birthday}" for record in upcoming])


def show_help():
    """Функція для виведення допомоги щодо команд."""
    help_text = """
    Available commands:
    1. add [name] [phone] - Add a new contact or update phone number for an existing contact.
    2. change [name] [old phone] [new phone] - Change phone number for an existing contact.
    3. phone [name] - Show phone numbers for the specified contact.
    4. all - Show all contacts in the address book.
    5. add-birthday [name] [birthday] - Add a birthday for the specified contact (format: DD.MM.YYYY).
    6. show-birthday [name] - Show birthday for the specified contact.
    7. birthdays - Show upcoming birthdays for the next week.
    8. hello - Get a greeting message from the bot.
    9. close or exit - Close the program.
    """
    print(help_text)


def main():
    book = AddressBook()
    print("Welcome to the assistant bot! Type 'help' to see available commands.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone, *_ = args
            record = book.find(name)
            message = "Contact updated."
            if record is None:
                record = Record(name)
                book.add_record(record)
                message = "Contact added."
            if phone:
                record.add_phone(phone)
            print(message)

        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                record.edit_phone(old_phone, new_phone)
                print(f"Phone number for {name} updated.")
            else:
                print(f"Contact {name} not found.")

        elif command == "phone":
            name, *_ = args
            record = book.find(name)
            if record:
                print(f"{name}'s phones: {', '.join(phone.value for phone in record.phones)}")
            else:
                print(f"Contact {name} not found.")

        elif command == "all":
            for record in book.data.values():
                print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "help":
            show_help()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
