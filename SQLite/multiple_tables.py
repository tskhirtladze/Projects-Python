import sqlite3


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("DROP table students")
cursor.execute("DROP table courses")
cursor.execute("DROP table enrollments")

conn.commit()

# -----------------------------------------
# Create Tables
# -----------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    teacher TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_on DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

conn.commit()

# -----------------------------------------
# Insert Sample Data
# -----------------------------------------
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Alice Johnson", "alice@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Bob Smith", "bob@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Charlie Lee", "charlie@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Diana Brooks", "diana@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Ethan Carter", "ethan@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Fiona Adams", "fiona@example.com"))
cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("George Hunt", "george@example.com"))


cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Database Systems", "Dr. Miller"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Web Development", "Prof. Clark"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Machine Learning", "Dr. Ray"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Data Structures", "Dr. Lopez"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Networking Fundamentals", "Prof. Patel"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Cloud Computing", "Dr. Nguyen"))
cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", ("Cybersecurity Basics", "Dr. Watson"))


cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (1, 3))
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (2, 2))
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (3, 1, '2025-12-09'))
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (4, 5))   # Diana → Data Structures
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (4, 6))   # Diana → Networking
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (5, 1, "2025-12-09"))
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (5, 7, "2025-12-10"))
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (6, 2))   # Fiona → Web Dev
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (6, 8, "2025-12-11"))
cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (7, 3))   # George → Machine Learning
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (7, 4, "2025-12-09"))
cursor.execute("INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)", (7, 6, "2025-12-12"))


cursor.execute("""
    SELECT *
    FROM students
""")
students = cursor.fetchall()


cursor.execute("""
    SELECT *
    FROM courses
""")
courses = cursor.fetchall()

cursor.execute("""
    SELECT *
    FROM enrollments
""")
enrollments = cursor.fetchall()

print("Students Table:")
print(students, "\n")
print("Courses Table:")
print(courses, "\n")
print("Enrollments Table:")
print(enrollments, "\n")


# -----------------------------------------
# UPDATE
# -----------------------------------------

print("--- Updating student email ---")
cursor.execute("""
UPDATE students
SET email = ?
WHERE student_id = ?
""", ("alice.johnson@school.com", 1))

print("--- Updating course teacher ---")
cursor.execute("""
UPDATE courses
SET teacher = ?
WHERE course_id = ?
""", ("Dr. Hamilton", 3))  # Machine Learning


print("--- Updating enrollment date ---")
cursor.execute("""
UPDATE enrollments
SET enrolled_on = ?
WHERE enrollment_id = ?
""", ("2025-12-15", 2))  # Change Alice's second enrollment


# -----------------------------------------
# DELETE
# -----------------------------------------

print("--- Deleting a student ---")
cursor.execute("DELETE FROM students WHERE student_id = ?", (7,))


print("--- Deleting a course ---")
cursor.execute("DELETE FROM courses WHERE course_id = ?", (8,))


print("--- Deleting an enrollment ---")
cursor.execute("DELETE FROM enrollments WHERE enrollment_id = ?", (5,))




conn.commit()

cursor.execute("""
    SELECT *
    FROM students
""")
students = cursor.fetchall()

cursor.execute("""
    SELECT *
    FROM courses
""")
courses = cursor.fetchall()

cursor.execute("""
    SELECT *
    FROM enrollments
""")
enrollments = cursor.fetchall()

print()
print("Students Table:")
print(students, "\n")
print("Courses Table:")
print(courses, "\n")
print("Enrollments Table:")
print(enrollments, "\n")


# -----------------------------------------
# Example JOIN Queries
# -----------------------------------------

print("\n--- Students and their courses ---")
cursor.execute("""
SELECT s.name, c.course_name, c.teacher
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
""")
for row in cursor.fetchall():
    print(row)

print("\n--- Course counts per student ---")
cursor.execute("""
SELECT s.name, COUNT(e.course_id)
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
""")
for row in cursor.fetchall():
    print(row)

print("\n--- Students in Database Systems ---")
cursor.execute("""
SELECT s.name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Database Systems'
""")
for row in cursor.fetchall():
    print(row)


# -----------------------------------------
# Find the teacher with the highest total enrollments
# -----------------------------------------

print("\n--- Teacher with most enrollments ---")
cursor.execute("""
SELECT c.teacher,
       COUNT(e.student_id) AS total_enrollments
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.teacher
ORDER BY total_enrollments DESC
LIMIT 1;
""")
for row in cursor.fetchall():
    print(row)



# -----------------------------------------
# Count enrollments per day (uses the enrolled_on column)
# -----------------------------------------

print("\n--- Enrollments per date ---")
cursor.execute("""
SELECT enrolled_on,
       COUNT(*) AS total_enrollments
FROM enrollments
GROUP BY enrolled_on
ORDER BY enrolled_on;
""")
for row in cursor.fetchall():
    print(row)



# -----------------------------------------
# GROUP BY - Count how many enrollments each course has.
# -----------------------------------------
print("Count how many enrollments each course has")
cursor.execute("""
SELECT course_id,
       COUNT(*) AS total_enrollments
FROM enrollments
GROUP BY course_id
""")
print(cursor.fetchall())


# -----------------------------------------
# Basic SELECT + WHERE (Start with 'a')
# -----------------------------------------
print("Get all students whose name contains 'a'.")
cursor.execute("""
SELECT *,
       student_id
FROM students
WHERE name LIKE 'a%'
""")
print(cursor.fetchall())


# -----------------------------------------
# HAVING + GROUP BY
# -----------------------------------------
print('Show courses that have more than 1 student enrolled.')
cursor.execute("""
SELECT course_id,
       COUNT(*) AS total
FROM enrollments
GROUP BY course_id
HAVING total > 1
""")
print(cursor.fetchall())


# -----------------------------------------
# Nested SELECT (Subquery) - Students enrolled in Machine Learning.
# -----------------------------------------
print('Students enrolled in Machine Learning')
cursor.execute("""
SELECT name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT course_id
        FROM courses
        WHERE course_name = 'Machine Learning'
    )
)
""")
print(cursor.fetchall())


# -----------------------------------------
# UNION (Multiple SELECT results combined) - Get a combined list of all student names and teacher names.
# -----------------------------------------
print('Get a combined list of all student names and teacher names.')
cursor.execute("""
SELECT name AS person
FROM students
UNION
SELECT teacher AS person
FROM courses
""")
print(cursor.fetchall())





conn.close()
