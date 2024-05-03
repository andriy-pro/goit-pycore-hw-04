import json


def get_cats_info(path):
    """
    Reads a text file containing data about cats and returns a list of dictionaries
    with each cat's information.

    Parameters
    ----------
    path : str
        The file path to read the cat data from.

    Returns
    -------
    list of dict
        A list of dictionaries, where each dictionary contains the id, name, and age
        of a cat as strings.

    Examples
    --------
    >>> cats_info = get_cats_info("path/to/cats_file.txt")
    >>> print(cats_info)
    [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"}
    ]
    """

    separator = ','
    format_error_msg = "ERROR: {err}Line {line_number} does not match expected format:\n{line}\n"
    cat_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if not line.strip():  # Skip empty lines
                    continue

                parts = line.strip().split(separator)
                if len(parts) == 3:
                    if not parts[2].isdigit():
                        err = 'The age of the cat must be provided as a non-negative integer.\n'
                        print(format_error_msg.format(err=err, line_number=line_number, line=line))
                        continue
                    cat_dict = {'id': parts[0], 'name': parts[1], 'age': parts[2]}
                    cat_list.append(cat_dict)
                else:
                    print(format_error_msg.format(err='',line_number=line_number, line=line))
                    continue

    except FileNotFoundError:
        print(f"Error: The file does not exist:\n{path}")
    except PermissionError:
        print(f"Error: No permission to access the file:\n{path}")
    except OSError as e:
        print(f"Error: An OS error occurred while opening the file:\n{e.strerror}")
    except Exception as e:
        print(f"Error: An unexpected error occurred:\n{e}")

    return json.dumps(cat_list, indent=4)


if __name__ == "__main__":
    cats_info = get_cats_info("./tests/cats_file.txt")
    print(cats_info)
