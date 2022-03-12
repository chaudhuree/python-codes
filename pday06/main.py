print('**** day 06 ****')
print('#### lambda function ####')
print('#### sort tuple or complex items ####')
items = [
    ('product2', 10),
    ('product1', 20),
    ('product3', 14)
]
print(f"default item:{items}")

# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1])  # function need to pass as key and do not call
print(items)

print('#### map ####')
x = map(lambda item: item[1], items)
y = list(map(lambda item: item[1], items))
print(x)
print(y)
for item in x:
    print(item)

print('#### filter list ####')
filter_item = list(filter(lambda item: item[1] >= 10, items))
print(filter_item)

print('#### list comprehensions ####')

filter_item_map_lc = [item[1] for item in items]
filter_item_filter_lc = [item for item in items if item[1] >= 20]
print(f"{filter_item_map_lc}, {filter_item_filter_lc}");































