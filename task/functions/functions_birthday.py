from decorators.decorators import input_error
from address_book.address_book import AddressBook
from contacts.contacts import Record


@input_error
def add_birthday(args, address_book:AddressBook):
    if len(args)!=2:
        raise ValueError("Invalid number of arguments.")
    name,birthday=args
    name = name.capitalize()
    record=address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError(f"{name} not found")  

@input_error
def show_birthday(args, address_book:AddressBook):
    name, *_ = args
    name = args[0].capitalize()
    record = address_book.find(name)
    if record:
        return record.show_birthday()
    else:
        raise KeyError(f"{name} not found")  

@input_error
def birthdays(address_book:AddressBook):
    return address_book.get_upcoming_birthdays()