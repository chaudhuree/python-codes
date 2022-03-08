print("day two")

# conditional statement
print("#########conditional statement##########")
temperature = 20
if temperature > 25:
    print("its so hot today")
    print("drink water")
elif temperature > 30:
    print("feeling suffocated")
else:
    print('the day is beautiful')
print("done")

#  Ternary Operator
# normal case
print("######### ternary operator ##########")

age = 21
"""
if age > 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)"""
# for ternary operator
message = "eligible" if age > 18 else "not eligible"
print(message)

print("######### logical operator ##########")
# and or not
# not reverse the value of a variable
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("eligible for loan")
else:
    print("not eligible for loan")
