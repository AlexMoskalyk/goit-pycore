from collections import UserDict
import re
from datetime import datetime, timedelta

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
    """Клас для зберігання дати народження контакту, перевірка формату DD.MM.YYYY."""
    def __init__(self, value):
        try:
            # Перевірка та перетворення на об'єкт datetime
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я, телефон та день народження."""
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

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday_str):
        """Метод для додавання дня народження до запису контакту."""
        self.birthday = Birthday(birthday_str)

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
        """Повертає список користувачів, яких потрібно привітати по днях на наступному тижні."""
        today = datetime.today()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                # Calculate the upcoming birthday within the next week
                days_until_birthday = (record.birthday.value.replace(year=today.year) - today).days
                if days_until_birthday <= 7 and days_until_birthday >= 0:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("15.12.1990")
book.add_record(john_record)

# Додавання запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("20.12.1992")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Пошук та виведення контактів з майбутніми днями народження
upcoming = book.get_upcoming_birthdays()
print("\nUpcoming birthdays within the next week:")
for record in upcoming:
    print(record)