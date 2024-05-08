import sys
from pathlib import Path
from colorama import Fore, Style, init

def visualize_directory_structure(path: Path, indent: str = ""):
    """
    Recursively visualize the structure of a directory, coloring directories and files.

    Parameters
    ----------
    path : Path
        The directory path whose structure is to be visualized.
    indent : str
        The indentation to use for visualization, indicating the depth of recursion.

    """
    if path.is_dir():
        print(f"{indent}{Fore.BLUE + Style.BRIGHT}{path.name}/{Style.RESET_ALL}")
        new_indent = indent + "    "
        items = list(path.iterdir())
        for item in sorted(items):
            visualize_directory_structure(item, new_indent)
    else:
        print(f"{indent}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

def main():
    """
    Main function to handle command line arguments and invoke directory visualization.
    """
    init()  # Initialize colorama to make terminal color work on all platforms
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: {sys.argv[0]} <path_to_directory>{Style.RESET_ALL}")
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path specified does not exist or is not a directory.{Style.RESET_ALL}")
        sys.exit(1)
    
    visualize_directory_structure(directory_path)

if __name__ == "__main__":
    main()
