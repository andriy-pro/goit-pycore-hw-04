import re


def total_salary(path: str) -> tuple:
    """
    Calculate the total and average salary from a file.

    This function reads a file where each line consists of a developer's name and
    their salary separated by a comma. It handles various edge cases like empty lines,
    incorrect formats and values.

    Parameters
    ----------
    path : str
        The file path of the text file containing salaries.

    Returns
    -------
    tuple
        A tuple containing the total sum of the salaries and the average salary.

    Examples
    --------
    >>> total_salary("./tests/salary_file.txt")
    (6000.00, 2000.00)
    """

    separator = ','
    format_error_msg = "ERROR: Line {line_number} does not match expected format:\n{line}\n"
    remove_whitespaces = re.compile(r"\s+").sub
    total_sum = 0
    count = 0

    def is_non_negative_float(value: any) -> bool:
        """
        Verify if a variable can be converted to a non-negative float.

        Parameters
        ----------
        value : any
            The variable to be converted to float.

        Returns
        -------
        bool
            Returns True if the variable can be converted to a non-negative float, otherwise False.
        """
        try:
            f_value = float(value)
            return f_value >= 0
        except ValueError:
            return False

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if not line.strip():  # Skip empty lines
                    continue

                parts = line.strip().split(separator)
                if 1 < len(parts) < 4:
                    part_two = remove_whitespaces("", parts[1].strip())
                    if not is_non_negative_float(part_two):
                        print(format_error_msg.format(line_number=line_number, line=line))
                        continue

                    if len(parts) == 2: # The simplest case, correct string format
                        salary = float(part_two)
                    else:
                        part_three = remove_whitespaces("", parts[2].strip())
                        if part_two.isdigit() and part_three.isdigit():
                        # The 2nd and 3rd parts are integers separated by a separator (comma),
                        # thus we assume these are 2 parts of a float number
                            salary = float(f"{part_two}.{part_three}")
                        else:
                            print(format_error_msg.format(line_number=line_number, line=line))
                            continue
                else:
                    print(format_error_msg.format(line_number=line_number, line=line))
                    continue

                total_sum += salary
                count += 1

        if count == 0: # Avoid division by zero if no valid entries were found
            return ('0.00', '0.00')

        average_salary = total_sum / count
        return f"{round(total_sum, 2):.2f}", f"{round(average_salary, 2):.2f}"

    except FileNotFoundError:
        print(f"Error: The file does not exist:\n{path}")
    except PermissionError:
        print(f"Error: No permission to access the file:\n{path}")
    except OSError as e:
        print(f"Error: An OS error occurred while opening the file:\n{e.strerror}")
    except Exception as e:
        print(f"Error: An unexpected error occurred:\n{e}")


if __name__ == "__main__":
    total, average = total_salary("./tests/salary_file.txt")
    print(f"Total salary sum: {total}\nAverage salary: {average}")
