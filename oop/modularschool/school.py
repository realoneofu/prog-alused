"""School class which stores information about courses and students."""
# from course import Course
# from student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        pass
    
    def add_student(self, student):
        if student not in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)
        pass
    
    def add_student_grade(self, student, course, grade):
        if student in self.students and course in self.courses:
            student.add_grade(course,grade)
            course.grades.append(tuple([student,grade]))
        pass
    
    def get_students(self):
        return self.students
        pass
    
    def get_courses(self):
        return self.courses
        pass
    
    def get_students_ordered_by_average_grade(self):
        s_ordered = []
        lastgrade = 0
        for student in self.students:
            if student.get_average_grade() > lastgrade:
                s_ordered.insert(0, student)
                lastgrade = student.get_average_grade()
            else:
                s_ordered.insert(-1, student)
                lastgrade = student.get_average_grade()
        return s_ordered         
        pass
    
    
    pass

