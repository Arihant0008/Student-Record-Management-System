# 📘 Database-Driven-Student-Record-Management-System
This is a **Database-Driven Student Record Management System** developed using **Python**, the **Tkinter** GUI library (enhanced with `ttkthemes`), and a **MySQL** database backend. It follows a clean architecture with separate GUI and Database Management layers.

---

## 📌 Key Features

- **Comprehensive CRUD Operations:** Add, Search, Update, and Delete student records.
- **Data Integrity:** Includes validation for required fields and integer Roll Numbers.
- **Search Capabilities:** Search students by **Roll Number**, **Name**, or **Subject**.
- **Dynamic Table View:** Displays all records in a responsive `Treeview` widget.
- **📊 Data Visualization:** Generates a **Grade Distribution Pie Chart** using `matplotlib`.
- **📁 Data Export:** Exports all student data to an **Excel (`.xlsx`) file** using `pandas`.
- **Themed UI:** Uses `ttkthemes` for a modern, professional look (e.g., 'arc' theme).
- **Status Bar:** Provides real-time feedback on operations (success, errors, record counts).

---

## 🖥️ Architecture and GUI Framework

The application is split into two main components:

| Component | File | Role |
| :--- | :--- | :--- |
| **GUI Layer** | `main_app.py` | Handles all user interaction, form creation, data validation, and displaying results. |
| **Database Layer** | `database_manager.py` | Manages the MySQL connection and executes all CRUD/query logic. |

---

## 🗃️ Database Structure

Database Name: `student` (as per `database_manager.py`)
Table Name: `student`

You must configure your MySQL server with the following structure:

```sql
CREATE DATABASE student;

USE student;

CREATE TABLE student (
    rollNo INT PRIMARY KEY,
    name VARCHAR(100),
    fname VARCHAR(100),
    sub VARCHAR(100),
    grade VARCHAR(10)
);
```
**Note:** Ensure your database credentials in `database_manager.py` match your MySQL setup (e.g., `user="root"`, `password="Arihant123"`, `db="student"`).

## ⚙️ Requirements

**1. Python 3.x**

**2. MySQL Server**

**3. Required Python Libraries:**

```bash
pip install pymysql pandas openpyxl matplotlib ttkthemes
```
**Note:** Ensure your database credentials in `database_manager.py` match your MySQL setup (e.g., `user="root"`, `password="Arihant123"`, `db="student"`).

## ▶️ How to Run

1.  Start your MySQL Server and create the database and table as specified in the **Database Structure** section (from the full README).
2.  Clone or copy the project files (`main_app.py` and `database_manager.py`).
3.  Run the main application script:

```bash
python main_app.py
```
## 🧠 Key Functions in Code (`main_app.py` & `database_manager.py`)

| Function Name | Location | Purpose |
| :--- | :--- | :--- |
| `add_student_action()` | `main_app.py` | Validates data and calls the backend to insert a new student record. |
| `search_student_action()` | `main_app.py` | Retrieves and displays student(s) based on search criteria. |
| `update_student_action()` | `main_app.py` | Updates the selected field (name, subject, grade, etc.) for a student's roll number. |
| `show_delete_frame()` | `main_app.py` | Prompts for confirmation and calls the backend to remove a student record. |
| `populate_table()` | `main_app.py` | Refreshes the `Treeview` to display all current records. |
| `export_to_excel()` | `main_app.py` | Fetches all data, converts it to a `pandas.DataFrame`, and exports it to an Excel file. |
| `show_analytics_window()` | `main_app.py` | Fetches grade distribution data and displays a Pie Chart using `matplotlib`. |
| `DatabaseManager` methods | `database_manager.py` | All actual database interactions (`add_student`, `fetch_all_students`, etc.) are handled here. |
