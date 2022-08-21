from phonebook import contact_book


def command_error_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception as e:
            return str(e)
    return wrapper


def contact_validity(username: str):
    if contact_book.get(username) is not None:
        return True
    else:
        return False


def phone_validity(number: str):
    phone_number = (
        number.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if phone_number.isdigit() and phone_number.startswith("380") and len(phone_number) == 12:
        return True
    else:
        return False


@command_error_handler
def hello_handler():
    return f"Hello, how can I help you?"


@command_error_handler
def add_handler(username: str, number: str):
    if contact_validity(username):
        raise ValueError(f"Number with name '{username}' already exist in phonebook")
    else:
        if phone_validity(number):
            contact_book[username] = number
            return f"Contact with name '{username}' and number '{number}' was added successfully to phonebook"
        else:
            return f"Entered '{number}' is not a phone number.\nPlease use correct: start with '+380', 12 digits"


@command_error_handler
def change_handler(username: str, number: str):
    if contact_validity(username):
        if phone_validity(number):
            contact_book[username] = number
            return f"Number for contact '{username}' was changed successfully to '{number}'"
        else:
            return f"Entered '{number}' is not a phone number.\nPlease use correct: start with '380', 12 digits"
    else:
        raise ValueError(f"Number for contact '{username}' does not exist in phonebook. Please add it.")


@command_error_handler
def delete_handler(username: str):
    if username in contact_book.keys():
        contact_book.pop(username)
        return f"Contact '{username}' was deleted successfully from your phonebook"
    else:
        raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")


@command_error_handler
def phone_handler(username: str):
    if contact_validity(username):
        phone_number = contact_book.get(username)
        return f"Phone number of contact '{username}' is: '{phone_number}'"
    else:
        raise ValueError(f"Number is missed for the contact with name '{username}'")


@command_error_handler
def show_all_handler():
    if len(contact_book) == 0:
        return "Your phonebook is empty yet. Please add new contacts."
    else:
        first_string = "Your phonebook has the following contacts:\n"
        contact_lines = "\n".join(
            f"Name: {username}; Phone number: {number};" for (username, number) in contact_book.items()
        )
        return first_string + contact_lines


@command_error_handler
def exit_handler():
    raise SystemExit("\nThank you for cooperation. Good bye!\nSee you later. Stay safe.\n")


handlers_dict = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "delete": delete_handler,
    "phone": phone_handler,
    "show all": show_all_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
}

