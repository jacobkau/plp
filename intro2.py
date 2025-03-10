#integer - whole number
age = 23
#float - decimal number
height = 5.75
#string - text
name = "Charlie"
#boolean - true or false
is_student = True

# check the type of the variable
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(is_student)) # <class 'bool'>

# Dynamic Typing
# Python is a dynamically typed language. This means that the type of a variable is determined at runtime.
age = 25
print(age)
age = "Twenty Five"
print(age)
age = 25.0
print(age)