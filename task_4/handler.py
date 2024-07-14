import re

def validate_phone(phone: str):
    '''
    Simple phone number validation
    '''
    return re.match(r"[+?\d]", phone.strip())

def add_contact(args, contacts):
    '''
    Function add contacts
    '''
    if len(args) < 2:
        return "Error: invalid arguments. Usage: add NAME PHONE"
    name, phone = args

    if validate_phone(phone) is None:
        return "Phone number should contain only digits"

    if contacts.get(name):
        return "Contact already exist."

    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    '''
    Function change existing contacts
    '''
    if len(args) < 2:
        return "Error: invalid arguments. Usage: change NAME PHONE"
    name, phone = args

    if validate_phone(phone) is None:
        return "Phone number should contain only digits"

    if contacts.get(name) is None:
        return "Contact does not exist."

    contacts[name] = phone
    return "Contact changed."


def list_contacts(contacts):
    '''
    Function return all existing contacts
    '''
    output = ""
    for name, phone in contacts.items():
        output = f"{output}Contact: {name} - {phone}\n"
    return output

def show_phone(args, contacts):
    '''
    Function show phone of added contact
    '''
    name = args[0]
    phone = contacts.get(name)

    return phone if phone else "Contact not found"
