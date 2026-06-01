from models.subject import Subject
from database.db_manager import DatabaseManager

class SubjectService:

    def __int__(self):
        self.db = DatabaseManager()


    def create_subject(self, subject_name: str, class_id: int, subject_weight: float):

        query = """INSERT INTO subjects (subject_name, class_id, subject_weight) VALUES (?, ?, ?)"""

        subject_id, _ = self.db.execute_write(query, (subject_name, class_id, subject_weight))
        return subject_id
    
    
    def get_all_subjects(self):

        query = """SELECT id, subject_name, class_id, subject_weight FROM subjects"""

        rows = self.db.execute(query)
        subjects = []
        
        for row in rows:
            subjects.append(
                Subject(
                    id=row[0],
                    subject_name=row[1],
                    class_id=row[2],
                    subject_weight=row[3] 
                )
            )
            return subjects
        
        
    def get_subject_by_id(self, subject_id: int):

        query = """SELECT id, subject_name, class_id, subject_weight FROM subjects WHERE id = ?"""

        rows = self.db.execute(query, (subject_id,))

        if not rows:
            return None
        
        row = rows[0]

        return Subject(id=row[0], subject_name=row[1], class_id=row[2], subject_weight=row[3])
    
    
    def delete_subject(self, subject_id: int):#je dois ajouter une methode pour archiver plus tard

        query = """DELETE FROM subjects WHERE id = ?"""

        _, rowcount = self.db.execute_write(query, (subject_id, ))
        return rowcount > 0
    
    
    def update_subject(self, subject_id: int, subject_name: str, class_id: int, subject_weight: float):

        query = """UPDATE subjects SET subject_name = ?, class_id = ?, subject_weight = ? WHERE id = ?"""

        _, rowcount = self.db.execute_write(query, (subject_name, class_id, subject_weight, subject_id))

        return rowcount > 0
    
    
    def search_subjects(self, keyword: str):

        query = """SELECT id, subject_name, class_id, subject_weight FROM subjects WHERE subject_name LIKE ?"""

        rows = self.db.execute(query, (f"%{keyword}%", ))
        subjects = []

        for row in rows:
            subjects.append(
                Subject(
                    id=row[0],
                    subject_name=row[1],
                    class_id=row[2],
                    subject_weight=row[3]
                    )
            )
            return subjects
        
    
    def get_subjects_by_class(self, class_id: int):

        query = """SELECT id, subject_name, class_id, subject_weight FROM subjects WHERE class_id = ?"""

        rows = self.db.execute(query, (class_id, ))
        subjects = []

        for row in rows:
            subjects.append(
                Subject(
                    id=row[0],
                    subject_name=row[1],
                    class_id=row[2],
                    subject_weight=row[3]
                )
            )
            return subjects
        
        