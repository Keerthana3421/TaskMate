from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'taskmate_secret_key'

DATABASE = 'taskmate.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']

        # Hash the password
        password_hash = generate_password_hash(password)

        conn = get_db()
        try:
            conn.execute('INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)', 
                         (username, email, password_hash))
            conn.commit()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))

        except sqlite3.IntegrityError as e:
            print("Registration Error:", e)  # 🛠️ You will see the real reason in the terminal
            if 'username' in str(e):
                flash('Username already exists.')
            elif 'email' in str(e):
                flash('Email already exists.')
            else:
                flash('Registration failed. Please try again.')

        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        user = conn.execute('SELECT * FROM Users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    search = request.args.get('search', '')
    status_filter = request.args.get('status', '')

    conn = get_db()
    query = """
        SELECT t.task_id, t.title, t.due_date, t.status, t.priority,
               GROUP_CONCAT(c.category_name, ', ') AS categories
        FROM Tasks t
        LEFT JOIN TaskCategories tc ON t.task_id = tc.task_id
        LEFT JOIN Categories c ON c.category_id = tc.category_id
        WHERE t.user_id = ?
    """

    params = [session['user_id']]

    if search:
        query += " AND t.title LIKE ?"
        params.append(f"%{search}%")

    if status_filter:
        query += " AND t.status = ?"
        params.append(status_filter)

    query += " GROUP BY t.task_id ORDER BY t.due_date ASC"

    tasks = conn.execute(query, params).fetchall()
    conn.close()

    return render_template('dashboard.html', tasks=tasks, search=search, status_filter=status_filter)

# Route to handle task creation and category selection
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()

    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        status = request.form['status']
        priority = request.form['priority']
        selected_categories = request.form.getlist('categories')

        cur = conn.cursor()
        cur.execute('INSERT INTO Tasks (user_id, title, due_date, status, priority) VALUES (?, ?, ?, ?, ?)',
                    (session['user_id'], title, due_date, status, priority))
        task_id = cur.lastrowid

        for cat_id in selected_categories:
            cur.execute('INSERT INTO TaskCategories (task_id, category_id) VALUES (?, ?)', (task_id, cat_id))

        conn.commit()
        conn.close()
        flash('Task added successfully!')
        return redirect(url_for('dashboard'))

    
    categories = conn.execute('SELECT * FROM Categories').fetchall()
    conn.close()
    return render_template('add_task.html', categories=categories)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()
    task = conn.execute('SELECT * FROM Tasks WHERE task_id = ? AND user_id = ?', (task_id, session['user_id'])).fetchone()
    categories = conn.execute('SELECT * FROM Categories').fetchall()
    assigned = conn.execute('SELECT category_id FROM TaskCategories WHERE task_id = ?', (task_id,)).fetchall()
    assigned_ids = {cat['category_id'] for cat in assigned}

    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        status = request.form['status']
        priority = request.form['priority']
        selected_categories = request.form.getlist('categories')

        cur = conn.cursor()
        cur.execute('UPDATE Tasks SET title = ?, due_date = ?, status = ?, priority = ? WHERE task_id = ? AND user_id = ?',
                    (title, due_date, status, priority, task_id, session['user_id']))
        
        # Update categories
        cur.execute('DELETE FROM TaskCategories WHERE task_id = ?', (task_id,))
        for cat_id in selected_categories:
            cur.execute('INSERT INTO TaskCategories (task_id, category_id) VALUES (?, ?)', (task_id, cat_id))

        conn.commit()
        conn.close()
        flash('Task updated!')
        return redirect(url_for('dashboard'))

    conn.close()
    return render_template('edit_task.html', task=task, categories=categories, assigned_ids=assigned_ids)


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()
    conn.execute('DELETE FROM Tasks WHERE task_id = ? AND user_id = ?', (task_id, session['user_id']))
    conn.commit()
    conn.close()
    flash('Task deleted.')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
