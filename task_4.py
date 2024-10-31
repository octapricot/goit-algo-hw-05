# Cтворений декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

# Парсер команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Додана обробка помилок для команди add_contact
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added." 

# Додана обробка помилок для команди change_contact
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args 
    if name in contacts:
        contacts[name] = phone 
        return "Contact updated."
    else: 
        raise KeyError

# Додана обробка помилок для команди show_phone
@input_error
def show_phone(args, contacts): 
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError

# Додана обробка помилок для команди show_all
@input_error
def show_all(contacts): 
    if not contacts: 
        return "No contacts found."
    result = "All contacts:\n"
    for name, phone in contacts.items(): 
        result += f"{name}: {phone}\n"
    return result.strip()

# Основна функція програми
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]: 
            print("Goodbye!")
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()