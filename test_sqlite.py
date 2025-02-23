import sqlite3
conn = sqlite3.connect('pythonsqlite.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")

cursor.execute('''
INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 30)
''')

conn.commit()

cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

conn.close()