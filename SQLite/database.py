import sqlite3

# Connect to a database (Using memory)
# conn = sqlite3.connect(':memory:')

# Connect to a database
conn = sqlite3.connect('student.db')

# Create a cursor
cursor = conn.cursor()

# Data Types
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

cursor.execute("""
CREATE TABLE IF NOT EXISTS sample_data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score REAL,
    photo BLOB
)
""")

# read image as bytes
with open("pic.jpeg", "rb") as f:
    img_bytes = f.read()

# Insert records
cursor.execute(
    "INSERT INTO sample_data (id, name, score, photo) VALUES (?, ?, ?, ?)",
    (1, "Alice", 92.5, img_bytes)
)

cursor.execute('SELECT * FROM sample_data')
print(cursor.fetchone())

# Reading the BLOB back
cursor.execute("SELECT photo FROM sample_data WHERE id = 1")
photo_bytes = cursor.fetchone()[0]

with open("restored.jpg", "wb") as f:
    f.write(photo_bytes)

conn.commit()
conn.close()