# Exceptions

student = {
    'name': 'Mark',
    'student_id': 15163,
    'feedback': None
}

# add to the dictionary
#student['last_name'] = "Kowalski"

try:
    last_name = student["last_name"]
    #number_last_name = 3 + last_name
except KeyError as error:
    print("Error finding last_name")
    print(error)
except TypeError:
    print("I can't add these two together")
except Exception: # this will handle all the error
    print("Unknown error!")
finally: # this runs all the time
    print("DONE")

print("This code executes")