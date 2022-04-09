'''
    - There are no specific data structures for Stacks, 
      but we can accomplish what a stack does using Lists.
    
    - We create a list, call append() to add items to the end of the list,
      and call pop() to return objects from the end of the list.
'''



items = []

items.append('one')
items.append('two')
items.append('three')

print(items.pop())
print(items.pop())
print(items.pop())
print(items.pop())