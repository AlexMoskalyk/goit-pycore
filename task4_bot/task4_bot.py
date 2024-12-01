def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.
    """
    if len(args) != 2:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    """
    if len(args) != 2:
        return "Invalid input. Use: change [name] [phone]"
    name, phone = args
    if name not in contacts:
        return f"Contact {name} not found."
    contacts[name] = phone
    return f"Contact {name} updated."


def show_phone(args, contacts):
    """
    Повертає номер телефону для заданого імені.
    """
    if len(args) != 1:
        return "Invalid input. Use: phone [name]"
    name = args[0]
    if name not in contacts:
        return f"Contact {name} not found."
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    """
    Виводить всі контакти у форматі ім'я: номер телефону.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def show_help():
    """
    Показує список доступних команд.
    """
    return (
        "Available commands:\n"
        "  hello          - Greets you.\n"
        "  add [name] [phone] - Adds a new contact.\n"
        "  change [name] [phone] - Updates phone number for a contact.\n"
        "  phone [name]   - Shows the phone number of the contact.\n"
        "  all            - Shows all saved contacts.\n"
        "  help           - Shows this help message.\n"
        "  close/exit     - Exits the bot."
    )


def main():
    """
    Основний цикл обробки команд.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
