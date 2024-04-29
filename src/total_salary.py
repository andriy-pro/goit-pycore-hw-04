def total_salary(path: str) -> tuple:
    """
    Calculate the total and average salary from a file.

    This function reads a file where each line consists of a developer's last name and their salary separated by a comma.
    It handles various edge cases like empty lines, incorrect formats, and negative salaries.

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
    >>> total_salary("path/to/salary_file.txt")
    (6000, 2000)
    """

    format_error_msg = "Line {line_number} does not match expected format:\n{line}\n"
    total_sum = 0
    count = 0

    # Допоміжна функція, що перевіряє можливість конвертувати у тип 'float'
    def is_valid_non_negative_float(value: any) -> bool:
        """
        Перевіряє, чи довільна змінна містить лише одну крапку і може бути конвертована у додатне число типу float.

        Parameters
        ----------
        value : any
            Змінна, яку потрібно спробувати конвертувати до float.

        Returns
        -------
        bool
            Повертає True, якщо змінна має формат, який можна конвертувати до невід'ємного float.
        """
        # Конвертуємо у рядок
        value = str(value)

        # Перевіряємо, що в рядку лише одна крапка і що решта символів - цифри
        if value.count('.') == 1 and all(c.isdigit() or c == '.' for c in value):
            try:
                float(value)  # Спроба конвертації в float
                return True
            except ValueError:
                return False
        return False

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if not line.strip():  # Якщо рядок пустий, пропускаємо і переходимо до наступного
                    continue

                parts = line.strip().split(',')
                len_parts = len(parts)

                if 1 < len_parts < 4:
                    part_two = parts[1].strip()
                    if not(part_two.isdigit() or is_valid_non_negative_float(part_two)):
                        print(format_error_msg.format(line_number=line_number, line=line))
                        continue
                    if len_parts == 2: # Найпростіший випадок, вірний формат рядка
                        salary = float(part_two)
                    else:
                        part_three = parts[2].strip()
                        if part_two.isdigit() and part_three.isdigit():
                            # 2-га та 3-тя частини є цілими числами, розділеними комою, тому припускаємо,
                            # що це має бути число типу float
                            salary = float(f"{part_two}.{part_three}")
                        else:
                            print(format_error_msg.format(line_number=line_number, line=line))
                            continue
                else:
                    print(format_error_msg.format(line_number=line_number, line=line))
                    continue

                total_sum += salary
                count += 1

        if count == 0:
            return (0, 0)  # Avoid division by zero if no valid entries were found

        average_salary = total_sum / count
        return round(total_sum, 2), round(average_salary, 2)

    except FileNotFoundError:
        print(f"Error: The file does not exist:\n{path}")
    except PermissionError:
        print(f"Error: No permission to access the file:\n{path}")
    except OSError as e:
        print(f"Error: An OS error occurred while opening the file:\n{e.strerror}")
    except Exception as e:
        print(f"Error: An unexpected error occurred:\n{e}")

total, average = total_salary("./_tests/salary_file_1.txt")
print(f"Total salary sum: {total}\nAverage salary: {average}")