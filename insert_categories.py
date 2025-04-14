import sqlite3

conn = sqlite3.connect('taskmate.db')
cur = conn.cursor()

categories = [
    ('Work', 'Office tasks, meetings, and deadlines'),
    ('Personal', 'Self-care, daily chores'),
    ('Fitness', 'Health and wellness activities'),
    ('Career', 'Job hunting, resume updates'),
    ('Social', 'Events, calls, and catch-ups'),
    ('Finance', 'Budgeting, payments, banking'),
    ('Shopping', 'Buying essentials'),
    ('Travel', 'Planning trips, bookings'),
    ('Writing', 'Blogging, journaling'),
    ('Household', 'Cleaning, repairs')
]

for name, desc in categories:
    try:
        cur.execute("INSERT INTO Categories (category_name, description) VALUES (?, ?)", (name, desc))
    except sqlite3.IntegrityError:
        pass  # Already exists

conn.commit()
conn.close()

print("Categories inserted.")
