"""Student class with student name and grades."""
# from course import Course

class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        self.id = None
    
    def set_id(self, id: int):
        if self.id == None:
            self.id = id
        
    def get_id(self) -> int:
        return self.id
    
    def add_grade(self, course, grade):
        self.grades.append(tuple([course, grade]))
        pass
    
    def get_grades(self):
        return self.grades
        pass
    
    def get_average_grade(self):
        gradelen = len(self.grades)
        totalgrade = 0
        if gradelen > 0:
            for grade in self.grades:
                totalgrade += grade[1]
            return (totalgrade / gradelen)
        else:
            return -1
        pass
    
    def __repr__(self) -> str:
        return self.name
    
    pass
