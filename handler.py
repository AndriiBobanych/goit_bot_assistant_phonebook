from main import contact_book


def hello_handler():
    name_input = input("Hello! what is your name?\nPlease enter: ")
    return f"{name_input}, how can I help you?"


def contact_validity(username: str):
    if contact_book.get(username) is not None:
        return True
    else:
        return False


def add_handler(username: str, number: str):
    if contact_validity(username):
        raise ValueError(f"Number with name {username} already exist in phonebook")
    else:
        contact_book[username] = number
        return f"Contact with name {username} and phone number {number} was added to phonebook"


def change_handler(username: str, number: str):
    if contact_validity(username):
        raise ValueError(f"Number for contact {username} does not exist in phonebook. Please add it.")
    else:
        contact_book[username] = number
        return f"Number for contact {username} was changed successfully to {number}"


def phone_handler(username: str):
    if contact_validity(username):
        raise ValueError(f"Number is missed for the contact with name {username}")
    else:
        phone_number = contact_book.get(username)
        return f"Phone number of contact {username} is: {phone_number}"


def show_all_handler():
    if len(contact_book) == 0:
        return "Your phonebook is empty yet. Please add new contacts."
    else:
        first_string = "Your phonebook has the following contacts:\n"
        contact_lines = "\n".join(
            f"Name: {username}; Phone number is {number}" for (username, number) in contact_book.items()
        )
        return first_string + contact_lines


def exit_handler():
    raise SystemExit("Thank you for cooperation.\nSee you later. Stay safe.")


def unknown_handler(user_input: str):
    raise ValueError(f"Sorry. This command '{user_input}' is not valid. Please try again.")

