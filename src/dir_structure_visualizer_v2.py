import sys
from pathlib import Path
from colorama import Fore, Style, init

# Constants should be defined at the top level and be appropriately named.
MAX_ITEMS_COUNT = 100

def print_item(indent, symbol, item_name, color):
    """
    Print a formatted line with the specified indentation, symbol, color, and item name.

    Parameters
    ----------
    indent : str
        The indentation for the line.
    symbol : str
        The symbol to prepend to the item name (e.g. '┣━━', '┠──', '┗━━' or '┖──').
    item_name : str
        The name of the item to display.
    color : str
        The color code by colorama for the item name.
    """
    print(f"{Fore.YELLOW}{indent}{symbol}{color}{item_name}{Style.RESET_ALL}")

def visualize_directory_structure(path: Path, indent: str = ""):
    """
    Recursively prints the directory structure starting from the given path.

    Parameters
    ----------
    path : Path
        The directory path to visualize.
    indent : str, optional
        The indentation level for current visualization (default is empty).
    """
    items = list(path.iterdir())
    # Sorting items, directories first and then files
    items_sorted = sorted(items, key=lambda x: (x.is_file(), x.name.lower()))

    for i, item in enumerate(items_sorted):
        # Determining if the current item is not the last in the list
        last_item = i == len(items_sorted) - 1
        # Update the indent based on whether the item is the last
        new_indent = indent + ("    " if last_item else "┃   ")
        # Determine the symbol to use based on whether the item is the last and its type
        if item.is_dir():
            symbol = '┗━━ ' if last_item else '┣━━ '
            print_item(indent, symbol, f'📂 {item.name}', Fore.BLUE + Style.BRIGHT)
            visualize_directory_structure(item, new_indent)
        else:
            symbol = '┖── ' if last_item else '┠── '
            print_item(indent, symbol, f'📄 {item.name}', Fore.GREEN)

def main():
    """
    Main function to handle command line arguments and invoke directory visualization.
    """
    init()
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: {sys.argv[0]} <path_to_directory>{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    if not (directory_path.exists() and directory_path.is_dir()):
        print(f"{Fore.RED}Error: The specified path does not exist or is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    count = sum(1 for _ in directory_path.rglob('*'))
    if count > MAX_ITEMS_COUNT:
        print(f"{Fore.YELLOW}Number of items in the directory ({count}) exceeds the limit ({MAX_ITEMS_COUNT}).{Style.RESET_ALL}")
        if input(f"{Fore.YELLOW}Continue? (y/N): {Style.RESET_ALL}").strip().lower() != 'y':
            print(f"{Fore.YELLOW}Program terminated.{Style.RESET_ALL}")
            sys.exit(0)

    # Display the initial directory with the absolute path for better user control.
    print()
    print_item('', '', f'📦 {directory_path.resolve()}', Fore.BLUE)
    visualize_directory_structure(directory_path)
    print()


if __name__ == "__main__":
    main()
