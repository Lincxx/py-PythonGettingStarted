students = []

class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    #this return not the memory location, but something more readable
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def simple_method(self):
        pass


class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    #override methods
    def get_school_name(self):
        return "This is a high school student"

    #polymorpism
    def get_name_capitalize(self):
        #super refers to the parent class
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


john = HighSchoolStudent("james", 1234)
print(john.get_school_name())
print(john.get_name_capitalize())

