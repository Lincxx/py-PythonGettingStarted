# Lists

student_names = []
student_names = ["Mark", "Jeremy", "Tom"]

print(student_names[0])
print(student_names[2])

# get the first element from the right side of the list(or the last one)
print(student_names[-1])

# Replace a person

student_names[1] = "Ronda"
print(student_names)

# List Function

# add a new user
student_names.append("Jeremy")
print(student_names)

# check to see if an element exists
stillHere = "Mark" in student_names == True
print(stillHere)

if "Mark" in student_names:
    print(True)

# Get the length of a list
len(student_names)
print(len(student_names))

# Delete from a list
del student_names[2]
print(len(student_names))

# List Slicing, this doesn't alter the list
student_names[1:] # skips the first element and return the rest

student_names[1:-1] # skipe/ignores the first and last element





