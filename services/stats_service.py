from database.db_manager import DatabaseManager

class StatsService:

    def __init__(self):
        self.db = DatabaseManager()

    def get_student_average(self, student_id: str):

        query = """SELECT SUM(g.score * s.subject_weight) / SUM(s.subject_weight)
          FROM grades g JOIN subjects s ON g.subject_id = s.id WHERE g.student_id = ?"""

        rows = self.db.execute(query, (student_id,))
        if not rows or rows[0][0] is None:
            return None
        return rows[0][0]
    
    
    def get_subject_average(self, subject_id: int):

        query = """SELECT SUM(g.score) / COUNT(g.score) FROM grades g WHERE g.subject_id = ?"""

        rows = self.db.execute(query, (subject_id,))
        if not rows or rows[0][0] is None:
            return None
        return rows[0][0]
    

    def get_class_average(self, class_id: int):

        query = """SELECT SUM(g.score * s.subject_weight) / SUM(s.subject_weight)
          FROM grades g JOIN subjects s ON g.subject_id = s.id 
          JOIN students st ON g.student_id = st.id WHERE st.class_id = ?"""

        rows = self.db.execute(query, (class_id,))
        if not rows or rows[0][0] is None:
            return None
        return rows[0][0]