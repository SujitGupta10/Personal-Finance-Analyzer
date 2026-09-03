# Personal Expense Analyzer

A Python-based command-line application for recording and analyzing personal expenses. The application automatically assigns the current date to expenses and stores the data persistently in a JSON file.

## Features

* Add multiple expenses at once
* Automatically record the current date
* Categorize expenses
* Validate item, category, and amount inputs
* View all recorded expenses
* Calculate total expenses
* Calculate expenses by category
* Store expense data using JSON
* Preserve expense data between program runs

## Technologies Used

* Python
* JSON
* `datetime`

## Python Concepts Practiced

This project was built to strengthen understanding of core Python programming concepts, including:

* Variables and data types
* Lists
* Dictionaries
* Nested dictionaries
* Functions
* Loops
* Conditional statements
* User input and validation
* Exception handling
* File handling
* JSON serialization and deserialization
* Date and time handling

## Data Structure

The expense data is organized using a nested dictionary structure.

Each date acts as a key and contains:

* A list of expenses
* The total amount spent on that date

Example:

```json
{
    "03-09-2026": {
        "expenses": [
            {
                "Item": "Egg",
                "Category": "Food",
                "Amount": 20.0
            },
            {
                "Item": "Banana",
                "Category": "Fruit",
                "Amount": 30.0
            }
        ],
        "total": 50.0
    }
}
```

This structure allows expenses to be organized according to the date on which they were recorded.

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.json
└── README.md
```

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Expense-Tracker
```

Run the application:

```bash
python main.py
```

## Application Menu

```text
EXPENSE TRACKER

1. Add Expense
2. View Expense
3. Total Expense
4. Total Category Expense
5. Exit
```

## Data Persistence

The application uses a JSON file named `expenses.json` to store expense information.

When the program starts, previously saved expenses are loaded from the JSON file. New expenses are added to the existing data and saved back to the file.

This allows expense records to remain available even after the program is closed.

## Input Validation

The application validates user input to prevent invalid expense records.

Examples include:

* Item name cannot be empty
* Category cannot be empty
* Number of items must be a valid integer
* Expense amount must be a valid number
* Expense amount must be greater than zero

## Purpose

The purpose of this project was to build a practical Python application while improving my understanding of data structures, functions, file handling, JSON storage, input validation, and basic data analysis.

## Future Improvements

Possible improvements for future versions include:

* View expenses by a specific date
* Daily expense summaries
* Edit and delete expenses
* Monthly expense summaries
* Budget tracking
* Expense visualization
* CSV export
* Graphical user interface using Tkinter

## Author

**Sujit Gupta**

B.Tech Computer Science and Engineering (AI)
