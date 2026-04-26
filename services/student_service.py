import sqlite3

from models.student import Student
from database.db_manager import DatabaseManager

db = DatabaseManager()

class StudentService:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_student(self, last_name, first_name, gender, birth_date, parent_phone, class_id):
        query = """INSERT INTO students (student_id, last_name, first_name, gender, birth_date, parent_phone, class_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        params = (self.generate_student_id(), last_name, first_name, gender, birth_date, parent_phone, class_id)
        db.execute_write(query, params)
