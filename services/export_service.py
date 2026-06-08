from database.db_manager import DatabaseManager
from services.student_service import StudentService
from services.class_service import ClassService
from services.subject_service import SubjectService
from services.grade_service import GradeService

from openpyxl import Workbook

class ExportService:
    def __init__(self):
        self.db = DatabaseManager()
        self.students = StudentService()
        self.classes = ClassService()
        self.subjects = SubjectService()
        self.grades = GradeService()

    def export_all_data(self, filename: str = "school_data.xlsx"):
        
        wb = Workbook()

        #students sheet
        ws_students = wb.active
        ws_students.title = "Students"
        students = self.students.get_all_students()
        ws_students.append(["ID", "Student ID", "Last Name", "First Name", "Gender", "Birth Date", "Class ID", "Parent Phone", "Registration Date", "Active"])
        for s in students:
            ws_students.append([
                s.id, s.student_id, s.last_name, s.first_name, s.gender, 
                s.birth_date, s.class_id, s.parent_phone, s.registration_date, s.is_active
            ]) 

        #classes sheet
        ws_classes = wb.create_sheet(title="Classes")
        classes = self.classes.get_all_classes()
        ws_classes.append(["ID", "Class Name", "Class Level", "School Year", "Maximum Students", "Creation Date"])
        for c in classes:
            ws_classes.append([
                c.id, c.class_name, c.class_level, c.school_year, 
                c.maximum_students, c.creation_date
            ])

        #subjects sheet
        ws_subjects = wb.create_sheet(title="Subjects")
        subjects = self.subjects.get_all_subjects()
        ws_subjects.append(["ID", "Subject Name", "Subject Weight", "Class ID"])
        for sub in subjects:
            ws_subjects.append([
                sub.id, sub.subject_name, sub.subject_weight, sub.class_id
            ])

        #grades sheet
        ws_grades = wb.create_sheet(title="Grades")
        grades = self.grades.get_all_grades()
        ws_grades.append(["ID", "Student ID", "Subject ID", "Score", "Type", "Grade Date", "Comment"])
        for g in grades:
            ws_grades.append([
                g.id, g.student_id, g.subject_id, g.score, g.evaluation_type, g.evaluation_date, g.comment
            ])
        
        wb.save(filename)
        return filename