
Personal Data Manager | Python OOP Project

# Personal Data Manager | Python OOP Project

## About the Project

Personal Data Manager is a menu-driven Python application developed to manage personal journal entries using Object-Oriented Programming (OOP) and text-file handling.

The application allows users to add new entries, view saved entries, search by keyword or date, and delete all entries when required. Each entry is saved with a timestamp in `journal.txt`, so the data remains available after the program is closed.

This project demonstrates how Python classes, methods, file operations, and exception handling can be combined to build a practical application.

## Features

* **Add Journal Entries:** Save new entries with automatic date and time.

* **View All Entries:** Read and display previously saved entries.

* **Search Entries:** Search journal content using a keyword or date.

* **Delete All Entries:** Clear saved entries after user confirmation.

* **Automatic File Creation:** Create `journal.txt` if it does not exist.

* **Persistent Storage:** Keep journal data in a text file between program runs.

* **Exception Handling:** Handle common file errors and invalid menu selections.

* **Interactive Menu:** Repeat operations until the user chooses to exit.

## Technologies Used

* Python 3

* Object-Oriented Programming

* File Handling

* Exception Handling

* `datetime` module

## Project Structure

```
Personal-Data-Manager/
│
├── file_operator.py
├── journal.txt
└── README.md
```

* `file_operator.py` — Contains the `JournalManager` class and the main program logic.

* `journal.txt` — Stores journal entries and is created automatically when needed.

* `README.md` — Documents the project, its features, and how to run it.

## How to Run

1. Install Python 3.

2. Download or clone the project repository.

3. Open a terminal in the project directory.

4. Run the following command:

   python file_operator.py

5. Choose an option from the displayed menu.

## Menu Options

| Option | Description              |
| ------ | ------------------------ |
| 1      | Add a new journal entry  |
| 2      | View all journal entries |
| 3      | Search for an entry      |
| 4      | Delete all entries       |
| 5      | Exit the application     |

## Concepts Demonstrated

### 1. Object-Oriented Programming (OOP)

The project organizes its functionality inside the `JournalManager` class instead of placing all operations in separate, unrelated functions.

* **Class:** `JournalManager` defines the attributes and methods required to manage journal entries.

* **Object:** `my_journal = JournalManager()` creates an instance of the class.

* **Constructor:** `__init__()` initializes the private filename and checks whether the journal file exists.

* **Instance Methods:** `add_entry()`, `view_entry()`, `search_entry()`, `delete_entries()`, and `menu()` perform the application's operations.

### 2. Encapsulation

The filename is stored using the private attribute `self.__filename`. This demonstrates Python's name-mangling convention for restricting direct attribute access.

The file-management operations are grouped inside the class, keeping related functionality organized.

### 3. File Handling

The application uses Python's built-in file operations to store and retrieve data.

* `open()` opens a file in the required mode.

* `read()` retrieves saved content.

* `write()` saves or clears content.

* `close()` closes an opened file.

The project uses four file modes:

| Mode | Purpose                                               |
| ---- | ----------------------------------------------------- |
| `r`  | Read existing journal data                            |
| `w`  | Clear the file's existing content                     |
| `a`  | Add new entries without overwriting earlier entries   |
| `x`  | Create a new file only when it does not already exist |

### 4. Exception Handling

The program uses `try`, `except`, and `finally` to handle errors during file operations and user input.

* `FileNotFoundError` handles attempts to open a missing file.

* `PermissionError` handles file access or modification permission problems.

* `OSError` handles other operating-system-related file errors.

* `ValueError` handles invalid menu selections and empty search keywords.

The `finally` block checks whether the file was opened and closes it when necessary.

### 5. Date and Time Management

The `datetime` module generates the current date and time when an entry is added.

The timestamp is formatted as `YYYY-MM-DD HH:MM:SS`, making entries easier to identify and search.

### 6. Conditional Statements and Loops

The `if`, `elif`, and `else` statements process the user's menu choice and confirmation responses. The `while` loop keeps the menu running until the user selects the exit option.

### 7. String Operations

The application uses string methods such as `strip()` and `lower()` to validate empty input and perform case-insensitive searches.

The `split()` method separates stored entries for searching.

## Explanation Video

**Project walkthrough and code explanation**

* **Video Title:** Personal Data Manager in Python | OOP, File Handling and Exception Handling

* **Topics Covered:** Project introduction, class and object, constructor, encapsulation, file modes, adding and viewing entries, searching, deleting, exception handling, and program execution.

* **Video Link:** \(Add your explanation video URL here\)

## Connect With Me

* **LinkedIn:** [Vaidika Ghoghari](https://www.linkedin.com/in/vaidika-ghoghari-2196a534a)
* **Email:** [ghogharivaidika@gmail.com](mailto:ghogharivaidika@gmail.com)

Feel free to connect with me on LinkedIn or contact me by email to discuss Python projects, programming, and development.

## Future Improvements

* Edit an existing journal entry.

* Delete a selected entry instead of clearing the entire journal.

* Add password protection.

* Organize entries by date.

* Introduce a graphical user interface.

## Conclusion

Personal Data Manager is a practical Python project that demonstrates how OOP, file handling, exception handling, and basic data processing work together. Building this project provides hands-on experience in organizing code into a class, managing persistent text data, validating input, and handling common errors.

