# goit-pycore-hw-04

[*Українська версія*](#uk)
<span id="en"></span>

## Table of Contents

1. [***""***](#task-1)
2. [***""***](#task-2)
3. [***""***](#task-3)
4. [***""***](#task-4)

---

### Task 1

**Develop the function `total_salary(path)` to analyze a file with developers' salaries.**

#### Input data:
- A text file where each line contains a developer's last name and their salary, separated by a comma, without spaces. For example:
```python
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

#### Requirements:
1. The function should take the file path as an argument `path`.
2. Pay attention to the file's encoding when opening it.
3. Calculate the total and average sums of the salaries.
4. Return a tuple of two numbers: the total sum and the average salary.

#### Recommendations:
- Use the context manager `with` for safe file reading.
- Apply the `split(',')` method to separate information in each line.
- Handle potential errors when opening or reading the file.

#### Evaluation Criteria:
- The function must accurately determine the total and average sums.
- There should be error handling for cases when the file is missing or corrupted.
- The code must be clean, structured, and comprehensible.

#### Example of usage:
```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary sum: {total}, Average salary: {average}")
```

#### Expected result:
```
Total salary sum: 6000, Average salary: 2000
```

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#завдання-1">Прочитати це солов'їною</a>
  <a href="#table-of-contents">Return to Table of Contents</a>
</div>

---

### Task 2

**Develop the function `get_cats_info(path)` to read a file with data about cats.**

#### Input data:
- A text file where each line contains a unique cat identifier, its name, and age, separated by a comma. For example:
```python
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

#### Requirements:
1. The function should take the file path as an argument `path`.
2. The file contains data about cats with an identifier, name, and age.
3. The function should return a list of dictionaries, each containing information about one cat.

#### Recommendations:
- Use the context manager `with` for safe file reading.
- Consider the file encoding when opening it.
- Apply the `split(',')` method to separate information in each line.
- Create a dictionary with keys "id", "name", "age" for each record and add it to the return list.
- Handle errors related to file access or reading.

#### Evaluation Criteria:
- The function must accurately process data and return the correct list of dictionaries.
- Proper exception and error handling must be implemented.
- The code should be clean, structured, and comprehensible.

#### Example of usage:
```python
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

#### Expected result:
```json
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"}
]
```

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#завдання-2">Прочитати це солов'їною</a>
  <a href="#table-of-contents">Return to Table of Contents</a>
</div>

---

### Task 3


<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#завдання-3">Прочитати це солов'їною</a>
  <a href="#table-of-contents">Return to Table of Contents</a>
</div>

---

### Task 4


<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#завдання-4">Прочитати це солов'їною</a>
  <a href="#table-of-contents">Return to Table of Contents</a>
</div>


***
***


[*English Version*](#en)
<span id="uk"></span>

## Зміст
1. [***"Середня та максимальна зарплата"***](#завдання-1)
2. [***"Файл з даними про котів"***](#завдання-2)
3. [***"Візуалізації структури директорії"***](#завдання-3)
4. [***"Консольного бот-помічник"***](#завдання-4)
---

### Завдання 1

**Розробити функцію `total_salary(path)` для аналізу файлу з заробітними платами розробників.**

#### Вхідні дані:
- Текстовий файл, де кожен рядок містить прізвище розробника та його заробітну плату, розділені комою, без пробілів. До прикладу:
```python
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

#### Вимоги:
1. Функція має приймати шлях до файлу як аргумент `path`.
2. При відкритті файлу приділити увагу кодуванню.
3. Обчислити загальну та середню суму заробітних плат.
4. Повернути кортеж із двох чисел: загальної суми та середньої заробітної плати.

#### Рекомендації:
- Використовувати менеджер контексту `with` для безпечного читання файлів.
- Застосувати метод `split(',')` для розділення інформації в кожному рядку.
- Обробляти можливі помилки при відкритті або читанні файлу.

#### Критерії оцінювання:
- Функція має точно визначати загальну та середню суми.
- Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
- Код має бути чистим, структурованим і зрозумілим.

#### Приклад використання:
```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
```

#### Очікуваний результат:
```
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
```

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#task-1">Read this in English</a>
  <a href="#зміст">Повернутися до змісту</a>
</div>

---

### Завдання 2

**Розробити функцію `get_cats_info(path)` для читання файлу з даними про котів.**

#### Вхідні дані:
- Текстовий файл, де кожен рядок містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. До прикладу:
```python
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

#### Вимоги:
1. Функція має приймати шлях до файлу як аргумент `path`.
2. Файл містить дані про котів з ідентифікатором, ім'ям і віком.
3. Функція має повертати список словників, кожен з яких містить інформацію про одного кота.

#### Рекомендації:
- Використовувати менеджер контексту `with` для безпечного читання файлу.
- Враховувати кодування файлу при його відкритті.
- Застосувати метод `split(',')` для розділення інформації в кожному рядку.
- Створити словник з ключами "id", "name", "age" для кожного запису та додати його до повертаємого списку.
- Обробляти помилки, пов'язані з доступом до файлу або його читанням.

#### Критерії оцінювання:
- Функція має точно обробляти дані і повертати коректний список словників.
- Має бути виконана належна обробка винятків та помилок.
- Код має бути чистим, структурованим і зрозумілим.

#### Приклад використання:
```python
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

#### Очікуваний результат:
```json
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"}
]
```

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#task-2">Read this in English</a>
  <a href="#зміст">Повернутися до змісту</a>
</div>

---

### Завдання 3

**Розробити скрипт для візуалізації структури директорії, використовуючи кольорове відображення імен піддиректорій та файлів.**

#### Вхідні дані:
- Шлях до директорії передається як аргумент командного рядка. Скрипт аналізує та візуалізує структуру цієї директорії.

#### Вимоги:
1. Створити віртуальне оточення для ізоляції залежностей проекту.
2. Використати бібліотеку `colorama` для кольорового виведення імен директорій та файлів.
3. Скрипт має приймати шлях до директорії як аргумент при запуску.
4. Реалізувати рекурсивний спосіб обходу директорій для відображення їх структури.
5. Врахувати перевірку та обробку помилок, до прикладу, коли шлях не існує або не є директорією.

#### Рекомендації для виконання:
- Встановити `colorama` у віртуальному оточенні за допомогою `pip`.
- Використовувати модуль `sys` для отримання шляху до директорії як аргументу командного рядка.
- Для роботи з файловою системою використати модуль `pathlib`.
- Забезпечити належне форматування виводу, застосовуючи функції `colorama`.

#### Критерії оцінювання:
- Створення та використання віртуального оточення.
- Правильність отримання та обробки шляху до директорії.
- Точність виведення структури директорії.
- Коректне застосування кольорового виведення.
- Якість коду, включно з читабельністю, структуруванням та коментуванням.

#### Приклад використання:
```bash
python hw03.py /шлях/до/вашої/директорії
```

Цей скрипт виведе у терміналі список всіх піддиректорій та файлів у вказаній директорії, використовуючи різні кольори для піддиректорій та файлів, що сприяє кращому візуальному сприйняттю.

Для директорії зі наступною структурою
```
📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg
```
скрипт повинен вивести схожу структуру:

![Приклад виводу скрипта](hw-04_3_example-1.png)

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#task-3">Read this in English</a>
  <a href="#зміст">Повернутися до змісту</a>
</div>

---
### Завдання 4

**Розробити консольного бота-помічника, який розпізнаватиме та відповідатиме на команди користувача.**

#### Вхідні дані:
- Бот має працювати як консольний застосунок CLI (Command Line Interface) та обробляти команди, введені через клавіатуру.

#### Вимоги:
1. Програма повинна включати функцію `main()`, яка управляє основним циклом обробки команд.
2. Реалізувати функцію `parse_input()`, що аналізуватиме введений рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
3. Програма має очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. При введенні команд "exit" або "close", програма завершує роботу.
4. Реалізувати функції обробники для різних команд, такі як `add_contact()`, `change_contact()`, `show_phone()`.
5. Використовувати словник для зберігання імен та номерів телефонів. Ім'я буде ключем, номер телефону – значенням.
6. Програма повинна ідентифікувати та повідомляти про неправильно введені команди.

#### Опис команд:
- **hello**: Виводить "How can I help you?"
- **add [ім'я] [номер телефону]**: Додає контакт. Виводить "Contact added."
- **change [ім'я] [новий номер телефону]**: Оновлює існуючий контакт. Виводить "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено.
- **phone [ім'я]**: Показує номер телефону для зазначеного імені. Виводить номер телефону або повідомлення про помилку.
- **all**: Виводить усі збережені контакти з номерами.
- **close** або **exit**: Завершує роботу програми з виведенням "Good bye!".
- Якщо команда не відповідає жодному з форматів, виводить "Invalid command."

#### Рекомендації для виконання:
- Систематизувати опис форматів команд для бота-помічника, щоб зрозуміти, які функції потрібно реалізувати.
- Забезпечити належне тестування всіх команд перед впровадженням у продуктивне середовище.

#### Приклад виконання:
```bash
python assistant_bot.py
```
```plaintext
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: phone John
1234567890
Enter a command: exit
Good bye!
```

<div style="display: flex; justify-content: space-between; font-style: italic; font-size: smaller;">
  <a href="#task-4">Read this in English</a>
  <a href="#зміст">Повернутися до змісту</a>
</div>
