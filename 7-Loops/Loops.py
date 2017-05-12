# Loops

student_names = ["Mark", "Kat", "Rhonda", "Jessica"]

# for loops
for name in student_names:
    print(f"Student name is {name}")

x = 0
for index in range(10):
    x += 10
    print(f"The value of X is {x}...{index}")

# range function can support 2 args
for index in range(5, 10):
    x += 10
    print(f"The value of X is {x}...{index}")

# Well range function can support 3 args and the last being the increment
for index in range(5, 10, 2):
    x += 10
    print(f"The value of X is {x}...{index}")

# while loops