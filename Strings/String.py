string1 = 'this is a string'
string2 = "string"
string3 = """this is a string"""

txt = 'some,csv,values'

print(string1.capitalize())

print(string1.replace('i', 'w'))

print(string2.isalpha())

print(string2.isdigit())

print(txt)
print(txt.split(','))

#String Format Function

name = "PythonBo"
machine = "HAL"

print("Nice to meet you {0}. I am {1}".format(name, machine))

#String interpolation
print(f"Nice to meet you {name}. I am {machine}")

