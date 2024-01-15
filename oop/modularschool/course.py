"""Course class with name and grades."""
#from student import Student

class Course:
    
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    
    def get_grades(self):
        return self.grades
        pass
    
    def get_average_grade(self) -> float:
        gradelen = len(self.grades)
        totalgrade = 0
        if gradelen > 0:
            for grade in self.grades:
                totalgrade += grade[1]
            return (totalgrade / gradelen)
        else:
            return -1
        pass
    
    def __repr__(self):
        return self.name
        
    pass

