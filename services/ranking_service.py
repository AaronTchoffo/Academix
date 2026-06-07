from database.db_manager import DatabaseManager
from services.stats_service import StatsService
from models.student import Student

class RankingService:

    def __init__(self):
        self.db = DatabaseManager()
        self.stats = StatsService()

    def get_students_ranked(self):

        query = """SELECT id, student_id, last_name, first_name,
          gender, birth_date, class_id, parent_phone, registration_date, is_active FROM students
          WHERE is_active = 1"""

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
                class_id=row[6],
                parent_phone=row[7],
                registration_date=row[8],
                is_active=row[9]
            )
            
            average = self.stats.get_student_average(student.student_id)

            students.append({
                "student": student,
                "average": average            })

            students.sort(key=lambda x: x["average"], reverse=True)

            return students
        
    def get_student_rank(self, student_id: str):

        students = self.get_students_ranked()

        for index, entry in enumerate(students, start=1):
            if entry["student"].student_id == student_id:
                return index, entry["average"]
        return None, None
    

    def get_top_students(self, top_n: int = 5):

        students = self.get_students_ranked()

        return students[:top_n]

    
    def get_class_rankings(self, class_id: int):

        query = """SELECT id, student_id, last_name, first_name, gender, birth_date, class_id, parent_phone, registration_date, is_active FROM students
          WHERE class_id = ? AND is_active = 1"""
        
        rows = self.db.execute(query, (class_id,))

        students = []
        for row in rows:
            student = Student(
                id=row[0],
                student_id=row[1],
                last_name=row[2],
                first_name=row[3],
                gender=row[4],
                birth_date=row[5],
                class_id=row[6],
                parent_phone=row[7],
                registration_date=row[8],
                is_active=row[9]
            )
            average = self.stats.get_student_average(student.student_id)
            students.append({
                "student": student,
                "average": average
            })

        students.sort(key=lambda x: x["average"], reverse=True)
        return students


    def get_student_class_rank(self, student_id: str, class_id: int):

        students = self.get_class_rankings(class_id)

        for index, entry in enumerate(students, start=1):
            if entry["student"].student_id == student_id:
                return index, entry["average"]
        return None, None

       