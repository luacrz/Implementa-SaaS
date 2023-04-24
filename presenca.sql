CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    professor_id INTEGER NOT NULL,
    code INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(professor_id) REFERENCES users(id)
);

CREATE TABLE attendances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(class_id) REFERENCES classes(id),
    FOREIGN KEY(student_id) REFERENCES users(id)
);
