import re
from typing import Callable
from functools import wraps

## Dictionary of error messages
error_message = {
    "INVALID_PHONENUMBER": "Phone number should contain only digits",
    "INVALID_COMMAND": "Error: Invalid command.",
    "INVALID_ARGUMENTS": "Error: invalid arguments.",
    "UNKNOWN_COMMAND": "Error: Unknown command",
    "CONTACT_EXIST": "Contact already exist.",
    "CONTACT_NOT_FOUND": "Contact does not exist."
    }

def validate_phone(phone: str):
    '''
    Simple phone number validation
    '''
    return re.match(r"^\+?(\d+)$", phone.strip())

def input_error(func: Callable):
    '''
    Generic input decorator for validation user input
    '''
    @wraps(func)
    def inner(*args, **kwargs):
        action = func.__name__.split('_')

        ## Additional message hint to error message
        additional_message = ""
        match action[0]:
            case 'show':
                additional_message = "Usage: phone PHONE"
            case 'add' | 'change':
                additional_message = f"Usage: {action[0]} NAME PHONE"

        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_message["INVALID_ARGUMENTS"] + ' ' + additional_message
        except KeyError:
            return error_message["CONTACT_NOT_FOUND"]
        except IndexError:
            return error_message["INVALID_COMMAND"] + ' ' + additional_message

    return inner

def custom_error(func: Callable):
    '''
    Custom error decorator for validation
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"

    return inner


@custom_error
@input_error
def add_contact(args, contacts):
    '''
    Function add contacts
    '''
    name, phone = args

    if validate_phone(phone) is None:
        raise Exception(error_message["INVALID_PHONENUMBER"])

    if contacts.get(name):
        raise Exception(error_message["CONTACT_EXIST"])

    contacts[name] = phone
    return "Contact added."

@custom_error
@input_error
def change_contact(args, contacts):
    '''
    Function change existing contacts
    '''
    name, phone = args

    if validate_phone(phone) is None:
        raise Exception(error_message["INVALID_PHONENUMBER"])

    if contacts.get(name) is None:
        raise KeyError

    contacts[name] = phone
    return "Contact changed."


def list_contacts(contacts):
    '''
    Function return all existing contacts
    '''
    if not contacts:
        return "Contacts are empty"
    output = ""
    for name, phone in contacts.items():
        output = f"{output}Contact: {name} - {phone}\n"
    return output

@input_error
def show_phone(args, contacts):
    '''
    Function show phone of added contact
    '''
    name = args[0]
    phone = contacts[name]

    return phone
