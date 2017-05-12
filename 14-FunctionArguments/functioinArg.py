# Function Args

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

# A function with a default
def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

student_list = get_students_titlecase()

# named parameter
add_student("Mark", 15)


# A function with a variable number of args, the arg will return a list
def var_args(name, *args):
    print(name)
    print(args)

var_args("Mark", "Loves Python", None, "Hello", True)


# A function with a variable number of args called kwargs, which will return a dictionary
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["desc"], kwargs["feedback"])

var_kwargs("Mark", desc="Loves Python", feedback=None, subscriber=True)
