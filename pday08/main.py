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
