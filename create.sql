-- USERS table
CREATE TABLE Users (
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 username TEXT NOT NULL UNIQUE,
 email TEXT NOT NULL UNIQUE,
 password_hash BLOB NOT NULL, -- store as binary hash
 created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
-- TASKS table
CREATE TABLE Tasks (
 task_id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_id INTEGER,
 title TEXT NOT NULL,
 due_date TEXT,
 status TEXT CHECK (status IN ('Pending', 'In Progress', 'Completed')) DEFAULT 'Pending',
 priority TEXT CHECK (priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium',
 FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);
-- CATEGORIES table
CREATE TABLE Categories (
 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
 category_name TEXT NOT NULL UNIQUE,
 description TEXT
);
-- TASKCATEGORIES table
CREATE TABLE TaskCategories (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 task_id INTEGER,
 category_id INTEGER,
 notes TEXT,
 FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE,
 FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);