print('**** day 04 ****')
# project 01
# acronyms using python
print("#### acronyms ####")
# user_input = str(input("Enter a Phrase: "))
user_input = 'sohan chaudhuree'
text = user_input.split()
a = " "
for i in text:
    print(i)
    a = a + str(i[0]).upper()
print(a)

print("#### xargs ####")


def multiplication(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplication(2, 3, 6, 7))

print("#### xxargs (dictionary) ####")


def user_det(**details):
    print(details)
    print(details["name"])


user_det(id= 1, name= "chaudhuree", age= 26)
