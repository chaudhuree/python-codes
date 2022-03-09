print("****** day 03 ******")
print("####  ####")

print("#### define function ####")


def greeting():
    print('good mornig chaudhuree')


greeting()

print("#### function with argument ####")


def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")


greet("sOhan", "chaudhuree")

print("#### types of function ####")

"""
 1-perform a task
 2-return a value
 upper function are type one
 type two ⬇⬇
"""

def ret_func(name):
    return f"hi {name}"


message = ret_func("chaudhuree")
print(message)
