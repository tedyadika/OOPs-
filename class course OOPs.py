class Student: #class that contain student attributes 

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
    def get_age(self):
        return self.age

class course:
    def __init__(self, course_name, max_student):
        self.name = course_name
        self.max_student = max_student
        self.students = [] #creating an empty list to allow us add students to course 

    def add_student(self, student): #function to allow us add students to the list
        if len(self.students)< self.max_student:
            self.students.append(student)
            return True #returns true if successfully added 
        return False # returns false if not added

    def course_avg(self):
        total= 0
        for student in self.students:
            total += student.get_grade()
            return total/ len(self.students)
        




    

