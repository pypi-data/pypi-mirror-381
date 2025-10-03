PyElox: A Minimalist Web Framework
PyElox is a fast, secure, and compact Python web framework built from the socket up, designed for performance, modularity, and explicit control.

🚀 Quick Installation
To use PyElox, you need to install the core dependencies.

pip install python-dotenv Pillow
# Pyelox is not yet on PyPI, but after publication:
# pip install pyelox 

⚙️ Project Setup and Configuration (.env)
PyElox relies on a .env file in your project root for crucial settings, especially security.

Create a file named .env:

PYELOX_DEBUG=True
PYELOX_SECRET_KEY=A-STRONG-AND-UNIQUE-SECRET-KEY-FOR-SESSION-SECURITY
PYELOX_DB_NAME=data/pyelox.db

Debugging and Warnings
When PYELOX_DEBUG=True:

Detailed Tracebacks are displayed in the browser in English when an uncaught exception occurs.

Security Warnings are logged to the console (e.g., if PYELOX_SECRET_KEY is set to its default unsafe value, or if access comes from a loopback IP).

💡 Usage Example (APP.py)
This example demonstrates routing, templating, and initializing the database with a secure admin user.

from pyelox import PyElox
from pyelox.security import hash_password
from pyelox.sql import CREATE_USERS_TABLE, SELECT_ADMIN_USER, INSERT_USER

app = PyElox()

def _setup_db():
    try:
        app.db.execute_query(CREATE_USERS_TABLE)
    except Exception:
        pass

    # Check if admin exists using the secure fetch_query method
    if not app.db.fetch_query(SELECT_ADMIN_USER):
        admin_password_hash = hash_password('123')
        
        app.db.execute_query(
            INSERT_USER, 
            ['admin', admin_password_hash, 'Administrator']
        )

@app.route('/')
def index(request):
    return app.render('login.html', message="Please Log In")

@app.route('/dashboard')
def dashboard(request):
    username = request.get_query('user', 'Guest')
    return app.render('dashboard.html', username=username)

if __name__ == '__main__':
    _setup_db()
    app.run(host='127.0.0.1', port=8000)

🔑 Core Architecture Details
1. Database Management (pyelox/db.py)
PyElox abstracts SQLite connections, handling concurrent access via threading locks, and ensures connection hygiene to prevent the Cannot operate on a closed database error.

Method

Purpose

Return Type

Usage

execute_query(sql, params)

Write Operations (CREATE, INSERT, UPDATE, DELETE). Commits changes.

sqlite3.Cursor (Do not call fetch methods on it).

app.db.execute_query(INSERT_USER, ['user', hash, 'Role'])

fetch_query(sql, params)

Raw Read Operations (SELECT). Executes query, fetches all results, and closes connection.

list of tuples (raw results).

data = app.db.fetch_query("SELECT id FROM users")

select(table, **filters)

High-Level Read (Recommended). Executes SELECT and converts results into a list of dict (key=column name).

list of dictionaries.

user = app.db.select('users', username='admin')

2. SQL Statements Centralization (pyelox/sql.py)
All raw SQL strings are stored in pyelox/sql.py as constants. This makes the application code cleaner and simplifies adapting to different database backends in the future.

3. Security Utilities (pyelox/security.py)
This module provides basic, essential security operations.

Function

Purpose

hash_password(password)

Securely hashes a plaintext password (currently using SHA-256).

verify_password(stored_hash, provided_password)

Safely compares a provided password against a stored hash using constant-time comparison.

4. Routing and Requests
Method

Purpose

@app.route(path)

Registers a view function for a specific URL path, supporting variable routing (/user/<id>).

request.get_form(key)

Retrieves data from a submitted POST form.

request.get_query(key, default)

Retrieves data from URL query parameters (?key=value).

request.url_vars

Dictionary containing variables extracted from the route path (e.g., the id in /user/<id>).