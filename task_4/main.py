import handler

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(handler.add_contact(args, contacts))
            case "change":
                print(handler.change_contact(args, contacts))
            case "phone":
                print(handler.show_phone(args, contacts))
            case "all":
                print(handler.list_contacts(contacts))
            case _:
                print(handler.error_message["UNKNOWN_COMMAND"])

if __name__ == "__main__":
    main()
