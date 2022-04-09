testing = ['one', 'two', 'three', 'four', 'five']

print(testing)
print('testing id: {}'.format(id(testing)))

testing.remove('one')

print(testing)
print('testing id: {}'.format(id(testing)))

testing.append('six')

print(testing)
print('testing id: {}'.format(id(testing)))

name = 'This is my name'

print(name)
print(id(name))

name = name + 'oh I forgot, this is not my name'

print(name)
print(id(name))
