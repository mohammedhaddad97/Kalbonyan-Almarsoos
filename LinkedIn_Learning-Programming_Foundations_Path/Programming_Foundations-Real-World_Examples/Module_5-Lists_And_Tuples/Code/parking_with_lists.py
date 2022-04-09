'''
    - Lists are used to store a bunch of data usually that are similar or of the same category.
        Ex: people = ['Person 1', 'Person 2', 'Person 3']

    - We can access items in a list by their indecies, and the first item in the list is at indes 0
        Ex: people[1] returns the second item in the list which is 'Person 2'

    - We can add new items to the  list
        Ex: people.append('Person 4')
            people = ['Person 1', 'Person 2', 'Person 3', 'Person 4']

    - We can insert new items to the list and that's different from append():
        apped(): automatically adds the item to the end of the list so it doesn't affect the order.
        insert(): shifts the order of all the items after it.
        
        Ex: people.insert(2, 'New Person')
        people = ['Person 1', 'Person 2', 'New Person', 'Person 3', 'Person 4']
    
    - We can pop an item out of the list and what pop() does is; it returns the item, then removes it
      from the list, and we do that by passing the index of the item we wanna pop..

      Ex: people.pop(1)
        'Person 2'
        people = ['Person 1', 'New Person', 'Person 3', 'Person 4']
    
    - We can also remove an item from the list, and the difference between remove() and pop()
      is that remove() doesn't return the item, it just removes it, and that's because we pass it
      the item itself and that means we know exactly what's gonna be removed, so no need to reutrn it
      again.

      Ex: people.remove('New Person')
        people = ['Person 1', 'Person 3', 'Person 4']
'''