# CS 665 Project 1 - TaskMate

## Student Details

- **Name**: Keerthana Gudipalli  
- **WSU ID**: S832X783 
- **Course**: CS 665 – INtroduction Database Systems 
- **Instructor**: Huabo Lu  
- **Semester**: Spring 2025  

---

## Project Title

**TaskMate: Personal Task Management System**

---

## GitHub Link

🔗 [https://github.com/Keerthana3421/TaskMate](https://github.com/Keerthana3421/TaskMate)

---

## Demo Video



---

## Project Description

TaskMate is a personal task manager web app built using Python Flask and SQLite. It allows users to create, manage, and organize their daily tasks.

### Features:
- User registration and login
- Add, view, edit, and delete tasks
- Set task status: Pending, In Progress, Completed
- Set priority: Low, Medium, High
- Assign multiple categories to a task
- Search tasks by title
- Filter tasks by status
- Clean and responsive UI using Bootstrap

---

## Tools & Technologies Used

| Tool/Tech       | Purpose                          |
|------------------|----------------------------------|
| Python (Flask)   | Backend web framework            |
| SQLite           | Relational database              |
| HTML + Jinja2    | Page templates and rendering     |
| CSS + Bootstrap  | UI design and styling            |
| Git & GitHub     | Version control and project hosting |

---

## Database Design

### Tables:
1. **Users** – Stores login info  
2. **Tasks** – Stores task info (title, status, priority, etc.)  
3. **Categories** – List of category names  
4. **TaskCategories** – Many-to-many link between tasks and categories

All tables are in 3NF with foreign keys and constraints.

---

## SQL Files Provided

- `create.sql` – Creates all tables  
- `insert.sql` – Inserts sample data  
- `crud.sql` – Sample SQL queries for CRUD (insert, select with joins, update, delete)

---

## Features Implemented

- User login and registration  
- Create and view tasks
- Edit and delete tasks  
- Assign multiple categories (many-to-many)  
- Set priority and status  
- Search by title  
- Filter by status  
- Responsive UI with CSS + Bootstrap  
- SQL joins used to fetch tasks with categories

---

## How to Run This Project

1. Clone the GitHub repo  
2. Open the folder in VS Code  
3. Install Flask

---

## Project Setup and Running

To run this Flask-based task manager on your local machine, follow these steps:

1. **Clone the GitHub repository**

```bash
git clone https://github.com/Keerthana3421/TaskMate.git

2. **Navigate into the project directory**
```bash
cd TaskMate

3. **Install all required packages (Flask)**
```bash
pip install flask

4. **To start the Flask server, run:**
```bash
python app.py

5. **Open your browser and go to:**
```bash
http://127.0.0.1:5000/

