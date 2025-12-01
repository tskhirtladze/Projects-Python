import sqlite3
from datetime import date

# ---------------------------------------------------------
# 1. CREATE TABLE students
# ---------------------------------------------------------

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS students;
""")

cur.execute("""
CREATE TABLE students (
    name TEXT,
    surname TEXT,
    age INTEGER,
    date_of_birth TEXT,
    profile_picture BLOB
);
""")

print("Table created.\n")

# Read picture bytes once
with open("pic.jpeg", "rb") as f:
    picture_data = f.read()

# ---------------------------------------------------------
# 2. INSERT ONE RECORD
# ---------------------------------------------------------

cur.execute("""
INSERT INTO students (name, surname, age, date_of_birth, profile_picture)
VALUES (?, ?, ?, ?, ?)
""", ("Alice", "Johnson", 20, "2005-01-12", picture_data))

print("Inserted 1 record.\n")

# ---------------------------------------------------------
# 3. INSERT 4 RECORDS (placeholder)
# ---------------------------------------------------------

students_to_insert = [
    ("Bob", "Miller", 22, "2003-03-02", picture_data),
    ("Charlie", "Smith", 19, "2006-06-22", picture_data),
    ("Dana", "White", 21, "2004-11-15", picture_data),
    ("Evan", "Brown", 23, "2002-07-08", picture_data)
]

cur.executemany("""
INSERT INTO students (name, surname, age, date_of_birth, profile_picture)
VALUES (?, ?, ?, ?, ?)
""", students_to_insert)

print("Inserted 4 records.\n")

# ---------------------------------------------------------
# 4. QUERY + FETCH ALL
# ---------------------------------------------------------

cur.execute("SELECT rowid, name, surname, age, date_of_birth FROM students")
records = cur.fetchall()

print("Fetched results:\n")

# ---------------------------------------------------------
# 5. PRINT RESULTS (formatted)
# ---------------------------------------------------------

for row in records:
    print(f"ROWID: {row[0]} | Name: {row[1]} {row[2]} | Age: {row[3]} | DOB: {row[4]}")

print("\nFormatting complete.\n")

# ---------------------------------------------------------
# 6. WHERE CLAUSE using rowid
# ---------------------------------------------------------

print("Querying where rowid = 1:\n")

cur.execute("""
SELECT rowid, name, surname FROM students WHERE rowid = 1
""")
print(cur.fetchone(), "\n")

# ---------------------------------------------------------
# 7. UPDATE RECORDS
# ---------------------------------------------------------

cur.execute("""
UPDATE students
SET age = age + 1
WHERE surname = 'Smith'
""")
print("Updated records where surname = 'Smith'\n")

# ---------------------------------------------------------
# 8. DELETE RECORDS
# ---------------------------------------------------------

cur.execute("""
DELETE FROM students
WHERE name = 'Bob'
""")
print("Deleted records where name = 'Bob'\n")

# ---------------------------------------------------------
# 9. ORDER RESULTS
# ---------------------------------------------------------

print("Ordered by age descending:\n")

cur.execute("""
SELECT rowid, name, surname, age
FROM students
ORDER BY age DESC
""")

for row in cur.fetchall():
    print(row)

print()

# ---------------------------------------------------------
# 10. AND / OR
# ---------------------------------------------------------

print("Using AND/OR:\n")

cur.execute("""
SELECT rowid, name, surname, age
FROM students
WHERE age > 20 OR surname = 'White'
""")

for row in cur.fetchall():
    print(row)

print()

# ---------------------------------------------------------
# 11. LIMIT RESULTS
# ---------------------------------------------------------

print("Limiting results to 2 rows:\n")

cur.execute("""
SELECT rowid, name, surname, age
FROM students
LIMIT 2
""")

for row in cur.fetchall():
    print(row)

print()

# ---------------------------------------------------------
# 12. DROP A TABLE
# ---------------------------------------------------------

cur.execute("DROP TABLE IF EXISTS old_students")
print("Dropped table 'old_students' if existed.\n")

# Finalize
conn.commit()
conn.close()

print("All operations completed successfully.")
