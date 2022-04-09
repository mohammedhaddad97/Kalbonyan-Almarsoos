'''
    - Sets are a data structure used to store unique data where order doesn't matter.

    - We can combine those sets.
    
    ++++
    additoins of this lesson
    ++++

    - We can return what's in one set and not in the other/others using the difference() method.
    - We can return what's in both/all sets by using the method intersection()
    - symmetric_difference() removes the common and returns the rest.

'''

# 8

highschool = set ([
    'Mohammed Abdo',
    'Mohammed Ramadan',
    'Khaled Taha',
    'Waleed Abdulghaffar',
    'Yasser Tolba',
    'Mohammed Farag',
    'Hamada Abdurrahman',
    'Ibrahim Samy'
])

# 5

middleschool = set ([
    'Mohammed Abdo',
    'Yasser Tolba',
    'Hamada Abdurrahman',
    'Ibrahim Samy',
    'Hussein Hassan'
])

# 5

primaryschool = set ([
    'Ibrahim Samy',
    'Mohammed Abdo',
    'Hareth Haddad',
    'Ayman Khaled',
    'Hussein Hassan'
])


# print()
# print(highschool)
# print()
# print(middleschool)
# print()
# print(primaryschool)
# print()

friends = highschool.union(middleschool)

# print(friends)
print(highschool.difference(middleschool))
print(highschool.symmetric_difference(middleschool))
print(highschool.intersection(middleschool))

