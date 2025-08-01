# 📘 Student Record Management System

This is a **Student Record Management System** developed using **Python**, **Tkinter** for the GUI, and **MySQL** for the database backend. It provides a simple interface for managing student data including adding, updating, searching, displaying, and deleting records.

---

## 📌 Features

- Add new student records
- Search students by:
  - Roll Number
  - Name
  - Subject
- Update student details (Name, Subject, Grade)
- Delete student records
- View all stored records in a tabular format (with scrollbars)
- All actions use a MySQL database (`rec`)

---

## 🖥️ GUI Framework

The app uses **Tkinter** with responsive layout and color-coded frames:
- **Option Panel** for actions (Add, Search, Update, Delete, Show All)
- **Details Frame** for displaying records
- **Dynamic Forms** for each action

---

## 🗃️ Database Structure

Database Name: `rec`  
Table Name: `student`

```sql
CREATE DATABASE rec;

USE rec;

CREATE TABLE student (
    rollNo INT PRIMARY KEY,
    name VARCHAR(100),
    fname VARCHAR(100),
    sub VARCHAR(100),
    grade VARCHAR(10)
);
```
## Requirements
Python 3.x

MySQL Server

Required Python libraries:
```
pip install pymysql
```
## How to Run
Start MySQL Server and create the database as shown above.

Clone or copy this project.

Run the Python script:
```
python student.py

```
##  Key Functions in Code
- addFun() – Insert a new student record

- searchFun() – Retrieve student(s) by given field

- updFun() – Update selected field for a student

- delFun() – Delete a student record

- showAll() – Display all records

- tabFun() – Treeview UI component with scrollbars
