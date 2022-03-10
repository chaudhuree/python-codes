print('**** day 04 ****')
# project 01
# acronyms using python
user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    print(i)
    a = a + str(i[0]).upper()
print(a)
