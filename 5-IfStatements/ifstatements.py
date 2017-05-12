number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

# Truthy value is any number other than 0(zero) and any non empty string
# Falsy vlaue is a 0, empty string,

# An if statement to check if something is just define, we don't care what it is.
text = "Python"
if text:
    print("Text is defined and truthy")

# Boolean
python_course = True
if python_course:
    print("This will execute")

aliens_found = None
if aliens_found:
    print("This will NOT execute")

# Check if condition is not true (Not If) here we have some options != the keyword not
number = 4
if number != 4:
    print("This will not execute")

python_course = True
if not python_course:
    print("This will also not execute")

# Check for Multiple If Conditions

number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

# One line also know as Ternary If Statements
a = 1
b = 2
c = "bigger" if a > b else "smaller"
print(c)
