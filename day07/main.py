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
