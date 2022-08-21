
def parser_error_handler(func):
    def wrapper(user_input: str):
        try:
            return func(user_input)
        except ValueError as e:
            print("Incorrect input.\nPlease check details and enter correct command.")
            return str(e)
        except KeyError as e:
            print("Incorrect input.\nPlease check details and enter correct command.")
            return str(e)
        except TypeError as e:
            print("Incorrect input.\nPlease check details and enter correct command.")
            return str(e)
    return wrapper


def hello_parser(user_input: str):
    return "hello", []


def add_parser(user_input: str):
    username, number = user_input.lstrip("add").strip().split(" ")
    if len(username) > 0 and len(number) > 0:
        username = username.capitalize()
        return "add", [username, number]
    else:
        raise ValueError


def change_parser(user_input: str):
    username, number = user_input.lstrip("change").strip().split(" ")
    if len(username) > 0 and len(number) > 0:
        username = username.capitalize()
        return "change", [username, number]
    else:
        raise ValueError


def delete_parser(user_input: str):
    input_list = user_input.lstrip("delete").strip().split(" ")
    username = input_list[0]
    if len(username) > 0:
        username = username.capitalize()
        return "delete", [username]
    else:
        raise ValueError


def phone_parser(user_input: str):
    input_list = user_input.lstrip("phone").strip().split(" ")
    username = input_list[0]
    if len(username) > 0:
        username = username.capitalize()
        return "phone", [username]
    else:
        raise ValueError


def show_all_parser(user_input: str):
    if user_input.lower().strip() == "show all":
        return "show all", []
    else:
        raise ValueError


def exit_parser(user_input: str):
    if user_input.lower().strip() == "good bye":
        return "exit", []
    elif user_input.lower().strip() == "close":
        return "exit", []
    elif user_input.lower().strip() == "exit":
        return "exit", []
    else:
        raise ValueError


parsers_dict = {
    "hello": hello_parser,
    "add": add_parser,
    "change": change_parser,
    "delete": delete_parser,
    "phone": phone_parser,
    "show all": show_all_parser,
    "good bye": exit_parser,
    "close": exit_parser,
    "exit": exit_parser,
}


@parser_error_handler
def parse_user_input(user_input: str) -> tuple[str, list]:
    for command in parsers_dict.keys():
        normalized_input = " ".join(user_input.lower().strip().split(" "))
        if normalized_input.startswith(command):
            parser = parsers_dict.get(command)
            return parser(user_input=normalized_input)
    raise ValueError

