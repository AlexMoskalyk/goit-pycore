import pickle

class AddressBook:
    def __init__(self):
        """
        Ініціалізуємо порожню адресну книгу.
        """
        self.contacts = {}

    def add_contact(self, name, phone, email):
        """
        Додає новий контакт до адресної книги.
        """
        self.contacts[name] = {"phone": phone, "email": email}

    def get_contact(self, name):
        """
        Отримує контакт за іменем.
        """
        return self.contacts.get(name, "Контакт не знайдено")

    def delete_contact(self, name):
        """
        Видаляє контакт за іменем.
        """
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Контакт не знайдено")

    def show_all_contacts(self):
        """
        Виводить усі контакти.
        """
        return self.contacts

    def __repr__(self):
        return f"AddressBook({self.contacts})"




def save_data(book, filename="addressbook.pkl"):
    """
    Зберігає адресну книгу у файл.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """
    Завантажує адресну книгу з файлу. Якщо файл не знайдено, повертає нову адресну книгу.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл не знайдено, створюється нова адресна книга.")
        return AddressBook()



def main():
    # Завантажуємо дані з файлу при старті програми
    book = load_data()

    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Показати всі контакти")
        print("3. Отримати контакт")
        print("4. Видалити контакт")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть email: ")
            book.add_contact(name, phone, email)
            print(f"Контакт {name} додано.")

        elif choice == "2":
            contacts = book.show_all_contacts()
            if contacts:
                for name, details in contacts.items():
                    print(f"{name}: Телефон: {details['phone']}, Email: {details['email']}")
            else:
                print("Адресна книга порожня.")

        elif choice == "3":
            name = input("Введіть ім'я для пошуку: ")
            contact = book.get_contact(name)
            print(contact)

        elif choice == "4":
            name = input("Введіть ім'я для видалення: ")
            book.delete_contact(name)

        elif choice == "5":
            # Зберігаємо дані у файл перед виходом
            save_data(book)
            print("Дані збережено. До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()