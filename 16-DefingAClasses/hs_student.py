from students import Student

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
