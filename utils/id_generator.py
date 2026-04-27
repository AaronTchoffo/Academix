from datetime import datetime

class IdGenerator:
    @staticmethod
    def generate_student_id(db):
        year = datetime.now().strftime("%y")
        prefix = f"{year}P"

        query = """SELECT student_id FROM students WHERE student_id LIKE ? ORDER 
        BY student_id DESC LIMIT 1"""
        result = db.execute(query, (f"{prefix}%", ))

        if not result:
            next_number = 1
        else:
            last_id = result[0][0]
            last_number = int(last_id.split("P")[1])
            next_number = last_number + 1
        
        return f"{prefix}{next_number:04d}"