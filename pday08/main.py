print('**** day 08 ****')
print('#### dictionary ####')
print('#### a way to declare dictionary ####')
point = {'x': 1, 'y': 2}
print('#### another way ####')
point_another = dict(a=3, b=4)
print(point, point_another)

print('#### to access value ####')
print(point['x'])
print(point_another['a'])

print('#### to set value or append new item ####')
point['x'] = 5
point['z'] = 6
print(point, point_another)

print('#### delete value ####')
del point['x']
print(point)

print('#### iterate ####')
for key in point:
    print(key, point[key])

print('#### another way to iterate ####')
for key, value in point.items():
    print(key, value)

print('#### dictionary comprehension ####')
# [expression for item in items]
# for dictionary
value_dictionary={x:x*2 for x in range(5)}
# for list
value_list=[x*2 for x in range(5)]
# set
value_set={x*2 for x in range(5)}
print(value_set,value_list,value_dictionary)

value_tuple=(x*2 for x in range(5))
print(value_tuple)

print('#### unpacking ####')
numbers=[1,2,3]
print(numbers)
print(*numbers)
num1=[1,2]
num2=[3,4]
num_combined=[*num1,5,*num2]
print(num_combined)
print('#### for dictionary ####')
first={'x':1}
second={'x':20,'y':2}
dict_combined={**first,**second}
print(dict_combined)














