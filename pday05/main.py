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










