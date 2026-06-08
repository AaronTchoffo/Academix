from database.db_manager import DatabaseManager
from models.classe import Class

class ClassService:
    def __init__(self):
        self.db = DatabaseManager()

    def create_class(self, class_name: str, class_level: str, school_year: str, maximum_students: int = 50):
        query = """INSERT INTO classes (class_name, class_level, school_year, maximum_students) 
                   VALUES (?, ?, ?, ?)"""
        class_id = self.db.execute_write(query, (class_name, class_level, school_year, maximum_students))
        return class_id
    
    def get_all_classes(self):

        query = "SELECT id, class_name, class_level, school_year, maximum_students, creation_date FROM classes"
        rows = self.db.execute(query)
        classes = []
        for row in rows:
            classes.append(Class(
                id=row[0],
                class_name=row[1],
                class_level=row[2],
                school_year=row[3],
                maximum_students=row[4],
                creation_date=row[5]
            ))
        return classes
    

    def get_class_by_id(self, class_id: int):
        query = "SELECT id, class_name, class_level, school_year, maximum_students, creation_date FROM classes WHERE id = ?"
        row = self.db.execute(query, (class_id,))

        row = row[0] if row else None
        if row:
            return Class(
                id=row[0],
                class_name=row[1],
                class_level=row[2],
                school_year=row[3],
                maximum_students=row[4],
                creation_date=row[5]
            )
        return None
    

    def update_class(self, class_id: int, class_name: str, class_level: str, school_year: str, maximum_students: int):
        query = """UPDATE classes 
                   SET class_name = ?, class_level = ?, school_year = ?, maximum_students = ? 
                   WHERE id = ?"""
        _, rowcount = self.db.execute_write(query, (class_name, class_level, school_year, maximum_students, class_id))
        return rowcount > 0
    

    def delete_class(self, class_id: int):
        query = "DELETE FROM classes WHERE id = ?"
        _, rowcount = self.db.execute_write(query, (class_id,))
        return rowcount > 0
    
    def search_classes(self, keyword: str):
        query = """SELECT id, class_name, class_level, school_year, maximum_students, creation_date 
                   FROM classes 
                   WHERE class_name LIKE ? OR class_level LIKE ? OR school_year LIKE ?"""
        like_term = f"%{keyword}%"
        rows = self.db.execute(query, (like_term, like_term, like_term))
        classes = []
        for row in rows:
            classes.append(Class(
                id=row[0],
                class_name=row[1],
                class_level=row[2],
                school_year=row[3],
                maximum_students=row[4],
                creation_date=row[5]
            ))
        return classes
    
    def get_class_student_count(self, class_id: int):
        query = """SELECT COUNT(*) FROM students WHERE class_id = ?"""
        row = self.db.execute(query, (class_id,))
        return row[0][0] if row else 0