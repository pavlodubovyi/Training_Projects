class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

matthewConnorGrades = [44, 53, 27, 60]
chloeMadisonGrades = [79, 58, 30, 66]
studentGrades = matthewConnorGrades, chloeMadisonGrades
matthewConnor = Student('Matthew', 'Connor', matthewConnorGrades)
chloeMadison = Student('Chloe', 'Madison', chloeMadisonGrades)
students = matthewConnor, chloeMadison