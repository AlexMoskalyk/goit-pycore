contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incomplete command. Please provide all required arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def list_contacts(_, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def delete_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return f"Contact {name} deleted."

def main():
    commands = {
        "add": add_contact,
        "phone": get_contact,
        "all": list_contacts,
        "delete": delete_contact,
    }

    while True:
        command_input = input("Enter a command: ").strip().split()
        if not command_input:
            print("Please enter a command.")
            continue

        command = command_input[0].lower()
        args = command_input[1:]

        if command == "exit":
            print("Goodbye!")
            break
        elif command in commands:
            result = commands[command](args, contacts)
            print(result)
        else:
            print("Unknown command. Available commands: add, phone, all, delete, exit.")

if __name__ == "__main__":
    main()
