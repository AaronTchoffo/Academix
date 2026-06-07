from models.student import Student
from database.db_manager import DatabaseManager
from utils.id_generator import IdGenerator


class StudentService:

    def __init__(self):
        self.db = DatabaseManager()


    def create_student(self, last_name, first_name, gender, birth_date, parent_phone, class_id):

        query = """INSERT INTO students (student_id, last_name, first_name, gender, birth_date, parent_phone, class_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        student_id = IdGenerator.generate_student_id(self.db)
        params = (student_id, last_name, first_name, gender, birth_date, parent_phone, class_id)
        self.db.execute_write(query, params)


    def get_all_students(self):

        query = """SELECT id, student_id, last_name,
          first_name, gender, birth_date, parent_phone, class_id, registration_date, is_active FROM students"""

        rows = self.db.execute(query)

        students = []
        for row in rows:
            student = Student(
                id=row[0],
                student_id=row[1],
                last_name=row[2],
                first_name=row[3],
                gender=row[4],
                birth_date=row[5],
                parent_phone=row[6],
                class_id=row[7],
                registration_date=row[8],
                is_active=bool(row[9])
            )
            students.append(student)

        return students
    
    
    def get_student_by_id(self, student_id:str):

        query = """SELECT id, student_id, last_name, 
        first_name, gender, birth_date, parent_phone, class_id, registration_date, is_active 
        FROM students WHERE student_id = ?"""

        result = self.db.execute(query, (student_id, ))

        if not result:
            return None
        
        row = result[0]

        student = Student(
            id=row[0],
            student_id=row[1],
            last_name=row[2],
            first_name=row[3],
            gender=row[4],
            birth_date=row[5],
            parent_phone=row[6],
            class_id=row[7],
            registration_date=row[8],
            is_active=bool(row[9])
        )

        return student


    def search_students(self, keyword:str):

        query = """SELECT id, student_id, last_name, 
        first_name, gender, birth_date, parent_phone, class_id, registration_date, is_active 
        FROM students WHERE (student_id LIKE ? OR last_name LIKE ? OR first_name LIKE ?) AND is_active = 1"""

        like_keyword = f"%{keyword}%"

        rows = self.db.execute(query, (like_keyword, like_keyword, like_keyword))

        students = []

        for row in rows:
            student = Student(
                id=row[0],
                student_id=row[1],
                last_name=row[2],
                first_name=row[3],
                gender=row[4],
                birth_date=row[5],
                parent_phone=row[6],
                class_id=row[7],
                registration_date=row[8],
                is_active=bool(row[9])
            )
            students.append(student)

        return students
    
    
    def update_student(self, student: Student):

        query = """UPDATE students SET last_name = ?, first_name = ?, gender = ?, birth_date = ?, parent_phone = ?
        , class_id = ?, is_active = ? WHERE student_id = ?"""

        params = (
            student.last_name,
            student.first_name,
            student.gender,
            student.birth_date,
            student.parent_phone,
            student.class_id,
            student.is_active,
            student.student_id
        )
        _, rowcount = self.db.execute_write(query, params)

        return rowcount > 0

    
    def delete_student(self, student_id:str):

        query = """DELETE FROM students WHERE student_id = ?"""

        _, rowcount = self.db.execute_write(query, (student_id, ))

        return rowcount > 0

    
    def archive_student(self, student_id:str):

        query = """UPDATE students SET is_active = 0 WHERE student_id = ? AND is_active = 1"""

        _, rowcount = self.db.execute_write(query, (student_id, ))

        return rowcount > 0

    def restore_student(self, student_id:str):

        query = """UPDATE students SET is_active = 1 WHERE student_id = ? AND is_active = 0"""

        _, rowcount = self.db.execute_write(query, (student_id, ))

        return rowcount > 0