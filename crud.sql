-- CREATE OPERATIONS:
-- 1. Add a new task for John_doe
INSERT INTO Tasks (user_id, title, due_date, status, priority)
VALUES (2, 'Prepare CS demo video', '2025-04-01', 'Pending', 'High');
-- 2.Add a new category
INSERT INTO Categories (category_name, description)
VALUES ('Chores', 'Household-related tasks');
-- READ OPERATIONS:
-- 1. Get all tasks for user_id 1
SELECT * FROM Tasks WHERE user_id = 1;
-- 2. Get all tasks with their categories
SELECT t.title, c.category_name
FROM Tasks t
JOIN TaskCategories tc ON t.task_id = tc.task_id
JOIN Categories c ON c.category_id = tc.category_id;
-- 3. UPDATE OPERATIONS:
-- 1. Change status of task_id 1 to 'Completed'
UPDATE Tasks SET status = 'Completed' WHERE task_id = 1;
-- 2. Change priority of 'Call Mom' to 'High'
UPDATE Tasks SET priority = 'High' WHERE title = 'Call Mom';
-- 3. Rename 'Personal' category to 'Lifestyle'
UPDATE Categories SET category_name = 'Lifestyle' WHERE category_name = 'Personal';
-- 4. DELETE OPERATIONS
-- 1. Remove task_id 10
DELETE FROM Tasks WHERE task_id = 10;
-- 2. Delete all tasks marked as 'Completed'
DELETE FROM Tasks WHERE status = 'Completed';
