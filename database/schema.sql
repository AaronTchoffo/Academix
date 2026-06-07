CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    creation_date TEXT DEFAULT CURRENT_TIMESTAMP,
    last_login TEXT
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    class_level TEXT NOT NULL,
    school_year TEXT NOT NULL,
    maximum_students INTEGER DEFAULT 50,
    creation_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('M', 'F')) NOT NULL,
    birth_date TEXT NOT NULL,
    parent_phone TEXT,
    class_id INTEGER REFERENCES classes(id),
    registration_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    subject_weight REAL NOT NULL DEFAULT 1.0,
    class_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
    UNIQUE(subject_name, class_id)
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    score REAL NOT NULL CHECK(score >= 0 AND score <= 20),
    evaluation_type TEXT DEFAULT 'exam',
    evaluation_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    comment TEXT
);

CREATE INDEX idx_grades_student ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject_id);
