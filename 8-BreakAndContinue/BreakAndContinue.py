# Breaks and Loop

student_names = ["Mark", "Kat", "Rhonda", "Jessica", "Tim", "Mary", "Bort", "Max"]


# Break will stop the loop
for name in student_names:
    if name == "Mark":
        print(f"Found him! {name}")
        break
    print(f"Currently testing {name}")

# Continue will skip the element found and continue on (no pun intended)
for name in student_names:
    if name == "Bort":
        continue # Because of this, the code below is unreachable
        print(f"Found him! {name}")
    print(f"Currently testing continue {name}")
