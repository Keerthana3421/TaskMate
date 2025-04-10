-- USERS
INSERT INTO Users (username, email, password_hash, created_at) VALUES
('keerthana', 'keerthana@email.com', X'6a9c9f7e8b1d', '2025-03-25 09:15:00'),
('john_doe', 'john@email.com', X'9f7e8b1d6a9c', '2025-03-26 10:30:00'),
('sara_k', 'sara@email.com', X'1d6a9c9f7e8b', '2025-03-27 08:45:00'),
('dev_g', 'dev@email.com', X'e8b1d6a9c9f7', '2025-03-28 11:00:00'),
('ananya', 'ananya@email.com', X'bbb444ccc999', '2025-03-28 14:20:00'),
('mike', 'mike@email.com', X'abcabcabc123', '2025-03-29 13:00:00'),
('leena', 'leena@email.com', X'defdef123456', '2025-03-29 15:10:00'),
('arjun', 'arjun@email.com', X'1234567890ab', '2025-03-30 09:00:00'),
('maya_r', 'maya@email.com', X'aaaa9999bbbb', '2025-03-30 16:45:00'),
('ravi_p', 'ravi@email.com', X'dddd8888eeee', '2025-03-31 08:00:00');
-- TASKS
INSERT INTO Tasks (user_id, title, due_date, status, priority) VALUES
(1, 'Complete SQL assignment', '2025-03-30', 'In Progress', 'High'),
(1, 'Buy groceries', '2025-04-01', 'Pending', 'Medium'),
(2, 'Team presentation', '2025-04-03', 'Pending', 'High'),
(3, 'Yoga class', '2025-04-02', 'Completed', 'Low'),
(4, 'Update resume', '2025-04-05', 'Pending', 'Medium'),
(5, 'Clean apartment', '2025-03-31', 'In Progress', 'Low'),
(6, 'Client follow-up', '2025-04-02', 'Pending', 'High'),
(7, 'Doctor appointment', '2025-04-01', 'Pending', 'Medium'),
(8, 'Book tickets', '2025-04-04', 'Pending', 'High'),
(9, 'Write blog post', '2025-04-06', 'In Progress', 'Medium');
-- CATEGORIES
INSERT INTO Categories (category_name, description) VALUES
('Work', 'Office tasks, meetings, and deadlines'),
('Personal', 'Self-care, daily chores'),
('Fitness', 'Health and wellness activities'),
('Career', 'Job hunting, resume updates'),
('Social', 'Events, calls, and catch-ups'),
('Finance', 'Budgeting, payments, banking'),
('Shopping', 'Buying essentials'),
('Travel', 'Planning trips, bookings'),
('Writing', 'Blogging, journaling'),
('Household', 'Cleaning, repairs');
-- TASKCATEGORIES
INSERT INTO TaskCategories (task_id, category_id, notes) VALUES
(1, 1, 'Submit to Blackboard by midnight'),
(2, 7, 'Milk, eggs, veggies'),
(3, 1, 'Prepare slides and talk track'),
(4, 3, 'Stretch and meditate after class'),
(5, 4, 'Include new certifications'),
(6, 10, 'Vacuum and mop floors'),
(7, 1, 'Email client the status update'),
(8, 5, 'Confirm time with doctor'),
(9, 8, 'Book via travel app'),
(10, 9, 'Topic: Productivity hacks');