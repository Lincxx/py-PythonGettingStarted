# Dictionaries key-value pairs, similar to JSON

student = {
    'name': 'Mark',
    'student_id': 15163,
    'feedback': None
}

print(student["name"])
# this will help us not get an error called KeyError
print(student.get("last_name", "Unknown"))

# Get all the key of the dict
print(student.keys())

# Get all the values of the dict
print(student.values())

# To reaname
student['name'] = "Fred"

# To delete - the key and value will be deleted
del student['then the key']

# To group a bunch of dictionaries put them in to a list

all_students = [
    {'name': 'Mark', 'student_id': 15163,'feedback': None },
    {'name': 'Steve', 'student_id': 15164,'feedback': None },
    {'name': 'Mary', 'student_id': 15165,'feedback': None }
]

print(all_students[1]["name"])




