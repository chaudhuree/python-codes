print('**** day 07 ****')
print('####  ####')
print('#### tuples (read only sequence) ####')

point = (1, 2)
print(type(point))
point_1 = (3, 4)
point_concatinate = point + point_1
print(point_concatinate)
print('#### convert list to tuple ####')
list_tuple = tuple([1, 2])
print(list_tuple)
print(tuple('sOhan'))

print('#### access ####')
print(point[0])
print(point[0:2])
print('#### unpack tuple ####')
x, y = point
print(x)
print('#### availabilty check ####')
if 10 in point:
    print('exist')

print('#### swaping variable ####')
a = 4
b = 6
a, b = b, a
print(a, b)

print('#### array ####')

from array import array

numbers = array('i', [1, 2, 3])
print(numbers)
numbers_last = numbers.pop()
print(numbers_last)

print('#### sets ####')
number_with_duplication=[1,1,2,2,3,4]
first=set(number_with_duplication)
print(f'number with duplicate:{number_with_duplication} \n unique value: {first} ')

second={1,5}
second.add(6)
print(second)

print('#### it can do mathematical operation ####')
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 3 in first:
    print('yes')















