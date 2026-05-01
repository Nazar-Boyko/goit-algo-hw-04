


def parse_input(user_input:str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    
    name, phone = args

    contacts[name] = phone
    return "Contacts added."


def change_contact(args,contacts):
    if len(args ) != 2:
        return "Usage: change [name] [phone]" 
    
    name, phone = args

    if contacts.get(name) is None:
        return "Contact not found."
    
    contacts[name] = phone  
    return "Contacts updated."

def show_phone(args,contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    
    name, = args

    if contacts.get(name) is None:
        return "Contact not found."
     
    return contacts[name]

def show_all(args, contacts : dict ):
    if not contacts:
        return "No contacts found."
    all_contacts = "\n".join(f"{name} {phone}" for name, phone in contacts.items())

    return all_contacts

def main():
    contacts = {}
    print("Welcome to assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close","exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can i help you?")

        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args,contacts))
        
        elif command == "phone":
            print(show_phone(args,contacts))

        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":

    main() 