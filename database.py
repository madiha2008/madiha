"""
Madiha Portfolio - Database Module
SQLite locally, PostgreSQL when DATABASE_URL is set (e.g. Render)
"""

import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'portfolio.db')
DATABASE_URL = os.environ.get('DATABASE_URL')
# Render sometimes uses postgres:// — psycopg expects postgresql://
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

IS_POSTGRES = bool(DATABASE_URL)

if IS_POSTGRES:
    import psycopg
    from psycopg.rows import dict_row

PH = '%s' if IS_POSTGRES else '?'


def get_connection():
    if IS_POSTGRES:
        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        return conn
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _execute(cursor, sql, params=None):
    if params is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, params)


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    if IS_POSTGRES:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                title TEXT,
                email TEXT,
                phone TEXT,
                about TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS skills (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                emoji TEXT,
                color TEXT,
                proficiency INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                technologies TEXT,
                image_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contact_messages (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                is_read INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitors (
                id SERIAL PRIMARY KEY,
                count INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    else:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                title TEXT,
                email TEXT,
                phone TEXT,
                about TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                emoji TEXT,
                color TEXT,
                proficiency INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                technologies TEXT,
                image_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contact_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                is_read INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                count INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    conn.commit()
    insert_default_data(conn)
    conn.close()
    print("🎀 Madiha's Database initialized!")


def insert_default_data(conn):
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) AS c FROM profile')
    row = cursor.fetchone()
    n = row['c'] if isinstance(row, dict) else row[0]
    if n == 0:
        q = f'''
            INSERT INTO profile (name, title, email, phone, about)
            VALUES ({PH}, {PH}, {PH}, {PH}, {PH})
        '''
        _execute(cursor, q, (
            'J Madiha Firdous',
            'BCA Student | Aspiring Web Developer',
            'madiha13052008@gmail.com',
            '9177702367',
            'I am a passionate BCA student with a deep interest in programming and web development. I love exploring new technologies and building creative solutions. My journey in tech started with curiosity, and now I am on a mission to become a skilled web developer. I believe in continuous learning and pushing boundaries.'
        ))

    cursor.execute('SELECT COUNT(*) AS c FROM skills')
    row = cursor.fetchone()
    n = row['c'] if isinstance(row, dict) else row[0]
    if n == 0:
        skills = [
            ('HTML5', '🌐', '#e34c26', 85),
            ('CSS3', '🎨', '#264de4', 80),
            ('Java', '☕', '#f89820', 75),
            ('Python', '🐍', '#3776ab', 70)
        ]
        q = f'''
            INSERT INTO skills (name, emoji, color, proficiency)
            VALUES ({PH}, {PH}, {PH}, {PH})
        '''
        for s in skills:
            _execute(cursor, q, s)

    cursor.execute('SELECT COUNT(*) AS c FROM projects')
    row = cursor.fetchone()
    n = row['c'] if isinstance(row, dict) else row[0]
    if n == 0:
        projects = [
            ('Portfolio Website 🎨', 'A fun cartoon-themed portfolio with playful animations!',
             'HTML,CSS,JavaScript,Python', 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400'),
            ('Calculator App 🔢', 'A colorful calculator with basic and scientific operations.',
             'HTML,CSS,JavaScript', 'https://images.unsplash.com/photo-1587145820266-a5951ee6f620?w=400'),
            ('To-Do List 📝', 'A cute task manager to organize daily activities!',
             'HTML,CSS,JavaScript', 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=400')
        ]
        q = f'''
            INSERT INTO projects (title, description, technologies, image_url)
            VALUES ({PH}, {PH}, {PH}, {PH})
        '''
        for p in projects:
            _execute(cursor, q, p)

    cursor.execute('SELECT COUNT(*) AS c FROM visitors')
    row = cursor.fetchone()
    n = row['c'] if isinstance(row, dict) else row[0]
    if n == 0:
        _execute(cursor, f'INSERT INTO visitors (count) VALUES ({PH})', (0,))

    conn.commit()


def _row_to_dict(row):
    if row is None:
        return None
    if isinstance(row, dict):
        return dict(row)
    return dict(row)


# Profile Operations
def get_profile():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM profile LIMIT 1')
    profile = cursor.fetchone()
    conn.close()
    return _row_to_dict(profile) if profile else None


# Skills Operations
def get_all_skills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM skills ORDER BY proficiency DESC')
    skills = [_row_to_dict(row) for row in cursor.fetchall()]
    conn.close()
    return skills


def add_skill(name, emoji, color, proficiency):
    conn = get_connection()
    cursor = conn.cursor()
    q = f'''
        INSERT INTO skills (name, emoji, color, proficiency)
        VALUES ({PH}, {PH}, {PH}, {PH})
    '''
    if IS_POSTGRES:
        q += ' RETURNING id'
        cursor.execute(q, (name, emoji, color, proficiency))
        skill_id = cursor.fetchone()['id']
    else:
        cursor.execute(q, (name, emoji, color, proficiency))
        conn.commit()
        skill_id = cursor.lastrowid
    if IS_POSTGRES:
        conn.commit()
    conn.close()
    return skill_id


# Projects Operations
def get_all_projects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
    projects = [_row_to_dict(row) for row in cursor.fetchall()]
    conn.close()
    return projects


def add_project(title, description, technologies, image_url):
    conn = get_connection()
    cursor = conn.cursor()
    q = f'''
        INSERT INTO projects (title, description, technologies, image_url)
        VALUES ({PH}, {PH}, {PH}, {PH})
    '''
    if IS_POSTGRES:
        q += ' RETURNING id'
        cursor.execute(q, (title, description, technologies, image_url))
        project_id = cursor.fetchone()['id']
    else:
        cursor.execute(q, (title, description, technologies, image_url))
        conn.commit()
        project_id = cursor.lastrowid
    if IS_POSTGRES:
        conn.commit()
    conn.close()
    return project_id


# Contact Messages Operations
def save_contact_message(name, email, message):
    conn = get_connection()
    cursor = conn.cursor()
    q = f'''
        INSERT INTO contact_messages (name, email, message)
        VALUES ({PH}, {PH}, {PH})
    '''
    if IS_POSTGRES:
        q += ' RETURNING id'
        cursor.execute(q, (name, email, message))
        message_id = cursor.fetchone()['id']
    else:
        cursor.execute(q, (name, email, message))
        conn.commit()
        message_id = cursor.lastrowid
    if IS_POSTGRES:
        conn.commit()
    conn.close()
    return message_id


def get_all_messages():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contact_messages ORDER BY created_at DESC')
    messages = [_row_to_dict(row) for row in cursor.fetchall()]
    conn.close()
    return messages


def mark_message_read(message_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'UPDATE contact_messages SET is_read = 1 WHERE id = {PH}', (message_id,))
    conn.commit()
    conn.close()


def delete_message(message_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM contact_messages WHERE id = {PH}', (message_id,))
    conn.commit()
    conn.close()


# Visitor Counter Operations
def get_visitor_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT count FROM visitors LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    if not result:
        return 0
    return result['count'] if isinstance(result, dict) else result[0]


def increment_visitor_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f'UPDATE visitors SET count = count + 1, last_updated = {PH}',
        (datetime.now(),)
    )
    conn.commit()
    cursor.execute('SELECT count FROM visitors LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    if not result:
        return 0
    return result['count'] if isinstance(result, dict) else result[0]


if __name__ == '__main__':
    init_database()
    print('✅ Database setup complete!')
