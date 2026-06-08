from database.db_manager import DatabaseManager
from services.student_service import StudentService
from services.grade_service import GradeService
from services.stats_service import StatsService
from services.ranking_service import RankingService
from services.class_service import ClassService

class ReportCardService:
    def __init__(self):
        self.db = DatabaseManager()
        self.students = StudentService()
        self.grades = GradeService()
        self.stats = StatsService()
        self.ranking = RankingService()
        self.classes = ClassService()


    def generate_report_report(self, student_id: str) -> dict:
        student = self.students.get_student_by_id(student_id)
        if not student:
            return None

        grades = self.grades.get_grades_by_student(student_id)
        rank, average = self.ranking.get_student_class_rank(student_id)
        total_students = self.classes.get_class_student_count(student.class_id)
        class_average = self.stats.get_class_average(student.class_id)

        report_card = {
            "student": student,
            "grades": grades,
            "average": average,
            "class_average": class_average,
            "rank": rank,
            "total_students": total_students
        }

        return report_card