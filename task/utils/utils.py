def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def print_menu():
    print("\nMenu:")
    print("1. Add contact")
    print("2. Change contact")
    print("3. Show phone")
    print("4. Show all contacts")
    print("5. Add birthday")
    print("6. Show birthday")
    print("7. Show upcoming birthdays")
    print("8. Delete contact")
    print("9. Close/Exit")