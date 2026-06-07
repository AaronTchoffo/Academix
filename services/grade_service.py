from models.grade import Grade
from database.db_manager import DatabaseManager

class GradeService:

    def __init__(self):
        self.db = DatabaseManager()

    def add_grade(self, student_id: str, subject_id: int, score: float, evaluation_type: str = "Exam", evaluation_date: str = None, comment: str = None) -> int:
        
        query = """INSERT INTO grades (student_id, subject_id, score,
          evaluation_type, evaluation_date, comment) VALUES (?, ?, ?, ?, ?, ?)"""
        
        grade_id, _ = self.db.execute_write(query, (student_id, subject_id, score,
                                                     evaluation_type, evaluation_date, comment))
        return grade_id


    def get_grades_by_student(self, student_id: str) -> list[Grade]:
        
        query = """SELECT id, student_id, subject_id, score, evaluation_type, evaluation_date, comment
                   FROM grades WHERE student_id = ?"""
        
        rows = self.db.execute(query, (student_id,))
        grades = []
        
        for row in rows:
            grades.append(Grade(
                id=row[0],
                student_id=row[1],
                subject_id=row[2],
                score=row[3],
                evaluation_type=row[4],
                evaluation_date=row[5],
                comment=row[6]
            ))
        
        return grades


    def get_grades_by_subject(self, subject_id: int) -> list[Grade]:
        
        query = """SELECT id, student_id, subject_id, score, evaluation_type, evaluation_date, comment
                   FROM grades WHERE subject_id = ?"""
        
        rows = self.db.execute(query, (subject_id,))
        grades = []
        
        for row in rows:
            grades.append(Grade(
                id=row[0],
                student_id=row[1],
                subject_id=row[2],
                score=row[3],
                evaluation_type=row[4],
                evaluation_date=row[5],
                comment=row[6]
            ))
        
        return grades


    def update_grade(self, grade_id: int,
                      score: float, evaluation_type: str = None, 
                      evaluation_date: str = None, comment: str = None) -> bool:
        
        query = """UPDATE grades SET score = ?, evaluation_type = ?, evaluation_date = ?, comment = ? WHERE id = ?"""
        
        _, rowcount = self.db.execute_write(query, (score, evaluation_type, 
                                                    evaluation_date, comment, grade_id))
        return rowcount > 0
    

    def delete_grade(self, grade_id: int) -> bool:
        
        query = """DELETE FROM grades WHERE id = ?"""
        
        _, rowcount = self.db.execute_write(query, (grade_id,))
        return rowcount > 0