# Intro to Database Project  
# TaskMate – A Personal Task Management System

TaskMate is a CRUD-based personal task manager web application developed using **Flask (Python)** for the backend, **SQLite** as the database, and **HTML/CSS with Bootstrap** for the frontend. This project demonstrates a database-driven web platform where users can manage their daily tasks, assign multiple categories, and filter/search by task status and title.

---

## Project Setup

### Database Setup

1. **Database Creation**:
   - The database schema is defined in `create.sql`.
   - Sample data is added using `insert.sql` which populates user, task, and category tables for testing.

2. **Database Connection**:
   - The app uses **SQLite** as its backend.
   - Running the app will automatically connect to or create `taskmate.db` using the structure defined in `create.sql`.

---

### Running the Application

1. **Install Required Packages**:
   - Navigate to the project folder and install Flask:
     ```bash
     pip install flask
     ```

2. **Start the Flask Server**:
   - Run the following command:
     ```bash
     python app.py
     ```

   - The app will run on **http://127.0.0.1:5000/** by default.

3. **Accessing the Application**:
   - Open your browser and go to `http://127.0.0.1:5000`
   - You can use the following routes:
     - **Register**: `/register`  
     - **Login**: `/login`  
     - **Dashboard**: `/dashboard`  
     - **Add Task**: `/add_task`  
     - **Edit Task**: `/edit_task/<task_id>`  
     - **Delete Task**: `/delete_task/<task_id>`  
     - **Logout**: `/logout`  

---

## Folder Structure

- **`create.sql`** – SQL to create all 4 tables in 3NF.
- **`insert.sql`** – Inserts sample data (users, categories, tasks).
- **`crud.sql`** – Example SQL commands (INSERT, SELECT with JOINs, UPDATE, DELETE).
- **`templates/`** – Contains all HTML templates (`base.html`, `dashboard.html`, etc.)
- **`static/`** – Contains CSS (`styles.css`) and image files.
- **`app.py`** – Flask app code with routes, logic, and database connections.

---

## Key Features

- **Secure User Authentication** – Separate accounts for each user.
- **CRUD Operations** – Users can create, read, update, and delete their tasks.
- **Task Attributes** – Each task has a title, due date, status, and priority.
- **Category Assignment** – Many-to-many mapping using a join table.
- **Search and Filter** – Users can search tasks by title or filter by status.
- **SQL JOINs** – Used to display categories linked to each task.
- **Bootstrap UI** – Responsive and styled user interface.

---

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2
- **Styling**: Bootstrap
- **Database**: SQLite
- **Version Control**: Git + GitHub

---

## Demo Video





## GitHub Repository

🔗 [https://github.com/Keerthana3421/TaskMate](https://github.com/Keerthana3421/TaskMate)

