from handler import handlers_dict
from parser import parse_user_input


def user_name_input():
    name_input = input("Hello! What is your name?\nPlease enter: ")
    print(f"\n{name_input.lower().capitalize()}, nice to meet you. let's start.\n")


def main():
    user_name_input()
    print("""You can use the following commands for your phonebook:
    - add name number - it's simple, to add new contact to your phonebook;
    - change name new-number - to set up new number for contact with this name (if exist);
    - delete name - to delete the contact with this name from phonebook (if exist);
    - phone name - to see the phone number for this name (if exist);
    - show all - to see all contacts in your phonebook (if you have added at least 1);
    - good bye / close / exit - to finish work and close session;
    """)
    while True:
        user_input = input("Please enter command: ")
        result = parse_user_input(user_input=user_input)
        if len(result) != 2:
            print(result)
            continue
        command, arguments = result
        command_handler = handlers_dict.get(command)
        try:
            command_response = command_handler(*arguments)
            print(command_response)
        except SystemExit as e:
            print(str(e))
            break


if __name__ == "__main__":
    main()

