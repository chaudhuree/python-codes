print('**** data structure ****')

print('#### creating list ####')
letters = ['a', 'b', 'c', 'd']
matrix = [[1, 2], [3, 4]]
zeros = [0] * 4
combine = letters + zeros
numbers = list(range(6))
chars = list('sOhan chaudhuree')
list_length = len(chars)
print(f"letters: {letters} \n list_of_list(matrix): {matrix} \n with command: {zeros} "
      f"\n combine two: {combine} \n using list and range: {numbers} \n itterate string: {chars} \n lengtg of list: {list_length}")

print('#### list accessing ####')
letters[0] = 'A'
print(letters[0])
print(letters[0:3])

print('#### copy a list ####')
print(letters[:])
print(letters[::2])  # step

numbers_one = list(range(20))
print('#### print all even ####')
print(numbers_one[::2])
print('#### reverse the list ####')
print(numbers_one[::-1])

print('#### unpacking list or destructuring ####')
numbers_two=list(range(8))

first,second,*other=numbers_two;
print(f"{first} \n {other}")

print('#### loop ####')
letters_one=['s','w','t']

for index,letter in enumerate(letters_one):
      print(index,letter)

print('#### adding and removing item in list ####')

letters_two=['a','b,','c','d']
print('#### add ####')
print('#### add last ####')
letters_two.append("e")
print(letters_two)
print('#### add at position ####')
letters_two.insert(2,'-')
print(letters_two)

print('#### delete ####')
print('#### remove last ####')
print(letters_two.pop())
print(letters_two)
print('#### at position ####')
print(letters_two.pop(2))
print(letters_two)
print('#### if we dont know the index ####')
letters_two.remove('a')
print('#### it will remove only first occurance. to remove all we have to loop over the list ####')
print(letters_two)
del letters_two[0:2]
print(letters_two)
print('#### clear all item in list ####')
letters_two.clear()
print(letters_two)


print('#### finding item in list ####')

letters_three=['a','b','c','d']
print('#### to know the index ####')
print(letters_three.index('c'))
print('#### to find number of time ,item available in list ####')
print(letters_three.count('e'))

print('#### availability check to avoid error ####')
if 'f' in letters_three:
      print(letters_three.index('f'))




























