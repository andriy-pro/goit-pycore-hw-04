import sys

from colorama import Fore, Style, init


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses the input from the user into a command and its arguments.

    Parameters
    ----------
    user_input : str
        The raw input string from the user.

    Returns
    -------
    tuple[str, list[str]]
        A tuple containing the command and a list of arguments.
    """
    parts = user_input.lower().split()
    command = parts[0] if parts else ''
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def hello() -> None:
    """
    Handles the 'hello' command by printing a helpful message.
    """
    print(f"{Fore.CYAN}How can I help you?{Style.RESET_ALL}")

def add_contact(contacts, *args):
    """
    Adds a new contact to the contact list or notifies if the contact already exists and updates it.
    Requires exactly two arguments, the name and phone number.

    Parameters
    ----------
    contacts : dict
        The dictionary containing the contacts.
    *args : tuple
        Arguments passed to the function, expected to be [name, phone].
    """
    if len(args) != 2:
        print(f"{Fore.RED}Invalid number of arguments. Usage: {Fore.YELLOW}add [name] [phone number]{Style.RESET_ALL}")
        return
    name, phone = args
    if name in contacts:
        if contacts[name] == phone:
            print(f'{Fore.YELLOW}Contact "{Fore.CYAN}{name}{Fore.YELLOW}" with phone number "{Fore.CYAN}{phone}{Fore.YELLOW}" already exists.{Style.RESET_ALL}')
        else:
            current_phone = contacts[name]
            print(f'{Fore.YELLOW}Contact "{Fore.CYAN}{name}{Fore.YELLOW}" is already added with the number "{Fore.CYAN}{current_phone}{Fore.YELLOW}".\nTo change the number, use the "{Style.RESET_ALL}change{Fore.YELLOW}" command.{Style.RESET_ALL}')
    else:
        contacts[name] = phone
        print(f'{Fore.GREEN}Contact "{Fore.CYAN}{name}{Fore.GREEN}" added with phone number "{Fore.CYAN}{phone}{Fore.GREEN}".{Style.RESET_ALL}')

def change_contact(contacts, *args):
    """
    Changes an existing contact's phone number if the new number is different from the current one.
    Requires exactly two arguments, the name and the new phone number.

    Parameters
    ----------
    contacts : dict
        The dictionary containing the contacts.
    *args : tuple
        Arguments passed to the function, expected to be [name, phone].
    """
    if len(args) != 2:
        print(f"{Fore.RED}Invalid number of arguments. Usage: {Fore.YELLOW}change [name] [new phone number]{Style.RESET_ALL}")
        return
    name, new_phone = args
    if name in contacts:
        current_phone = contacts[name]
        if new_phone == current_phone:
            print(f'{Fore.YELLOW}Contact "{Fore.CYAN}{name}{Fore.YELLOW}" already has this phone number: "{Fore.CYAN}{new_phone}{Fore.YELLOW}". No changes were made.{Style.RESET_ALL}')
        else:
            contacts[name] = new_phone
            print(f'{Fore.GREEN}For user {Fore.CYAN}"{name}"{Fore.GREEN}, the phone has been changed from "{Fore.CYAN}{current_phone}{Fore.GREEN}" to "{Fore.CYAN}{new_phone}{Fore.GREEN}".{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Contact with name "{Fore.CYAN}{name}{Fore.RED}" not found.{Style.RESET_ALL}')

def show_phone(contacts, name):
    """
    Shows the phone number for a specific contact.

    Parameters
    ----------
    contacts : dict
        The dictionary containing the contacts.
    name : str
        The name of the contact to lookup.
    """
    if name in contacts:
        print(f'{Fore.GREEN}Phone number of "{Fore.CYAN}{name}{Fore.GREEN}": {Fore.CYAN}{contacts[name]}{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Contact with name "{Fore.CYAN}{name}{Fore.RED}" not found.{Style.RESET_ALL}')

def show_all_contacts(contacts):
    """
    Displays all contacts and their phone numbers.

    Parameters
    ----------
    contacts : dict
        The dictionary containing the contacts.
    """
    if contacts:
        for name, phone in contacts.items():
            print(f'{Fore.GREEN}{name}: {Fore.CYAN}{phone}{Style.RESET_ALL}')
    else:
        print(f"{Fore.YELLOW}No contacts available.{Style.RESET_ALL}")

def handle_exit():
    """
    Handles the exit command to terminate the program.
    """
    print(f"{Fore.GREEN}{Style.BRIGHT}Good bye!{Style.RESET_ALL}")
    sys.exit()

def help_command():
    """
    Displays the help information with available commands.
    """
    print(f'{Fore.GREEN}This bot helps you manage your contacts.{Style.RESET_ALL}')
    print(f'{Fore.GREEN}You can use the following commands:{Style.RESET_ALL}')
    print(f'hello{Fore.GREEN} - Greets the user.{Style.RESET_ALL}')
    print(f'add [name] [phone number]{Fore.GREEN} - Adds a new contact.{Style.RESET_ALL}')
    print(f'change [name] [new phone number]{Fore.GREEN} - Changes the phone number of an existing contact.{Style.RESET_ALL}')
    print(f'phone [name]{Fore.GREEN} - Shows the phone number of a contact.{Style.RESET_ALL}')
    print(f'all{Fore.GREEN} - Shows all contacts.{Style.RESET_ALL}')
    print(f'close, exit, quit{Fore.GREEN} - Exits the program.{Style.RESET_ALL}')
    print(f'help{Fore.GREEN} - Displays a list of available commands.{Style.RESET_ALL}')
    print()
    print(f'{Fore.CYAN}Example usage:{Style.RESET_ALL}')
    print(f'add John 1234567890{Fore.GREEN} - Adds a contact named {Fore.CYAN}John{Fore.GREEN} with phone number {Fore.CYAN}1234567890.{Style.RESET_ALL}')
    print(f'phone John{Fore.GREEN} - Shows the phone number of {Fore.CYAN}John.{Style.RESET_ALL}')

def main():
    """
    Main function that runs the command line interface for an assistant bot.
    """
    contacts = {}
    command_handlers = {
        'hello': hello,
        'add': lambda args: add_contact(contacts, *args),
        'change': lambda args: change_contact(contacts, *args),
        'phone': lambda args: show_phone(contacts, *args),
        'all': lambda: show_all_contacts(contacts),
        'close': handle_exit,
        'exit': handle_exit,
        'quit': handle_exit,
        'help': help_command
    }

    init(autoreset=True)  # Initialize colorama

    banner_part_1 = """
 _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____ 
(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)
"""

    banner_part_2 = """
 _______  _______  _______ _________ _______ _________ _______  _       _________     ______   _______ _________
(  ___  )(  ____ \(  ____ \\\__   __/(  ____ \\\__   __/(  ___  )( (    /|\__   __/    (  ___ \ (  ___  )\__   __/
| (   ) || (    \/| (    \/   ) (   | (    \/   ) (   | (   ) ||  \  ( |   ) (       | (   ) )| (   ) |   ) (   
| (___) || (_____ | (_____    | |   | (_____    | |   | (___) ||   \ | |   | |       | (__/ / | |   | |   | |   
|  ___  |(_____  )(_____  )   | |   (_____  )   | |   |  ___  || (\ \) |   | |       |  __ (  | |   | |   | |   
| (   ) |      ) |      ) |   | |         ) |   | |   | (   ) || | \   |   | |       | (  \ \ | |   | |   | |   
| )   ( |/\____) |/\____) |___) (___/\____) |   | |   | )   ( || )  \  |   | |       | )___) )| (___) |   | |   
|/     \|\_______)\_______)\_______/\_______)   )_(   |/     \||/    )_)   )_(       |/ \___/ (_______)   )_(   
"""
    banner_part_3 = """
 _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____  _____ 
(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)(_____)
                                                                                                                
"""
    print(f'{Fore.GREEN}{banner_part_1}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}{Style.BRIGHT}{banner_part_2}{Style.RESET_ALL}')
    print(f'{Fore.GREEN}{banner_part_3}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}{Style.BRIGHT}Welcome to the Assistant Bot!{Style.RESET_ALL}')
    print()
    help_command()
    print()
    print()

    while True:
        user_input = input(f"{Fore.YELLOW}Enter a command: {Style.RESET_ALL}").strip()
        command, args = parse_input(user_input)
        if command in command_handlers:
            try:
                if args:
                    command_handlers[command](args)
                else:
                    command_handlers[command]()
            except TypeError:
                print(f"{Fore.RED}Invalid arguments provided for the command.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error processing command: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
