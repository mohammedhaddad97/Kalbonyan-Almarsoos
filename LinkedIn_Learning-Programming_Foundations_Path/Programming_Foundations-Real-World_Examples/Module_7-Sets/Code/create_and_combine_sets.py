'''
    - Sets are a data structure used to store unique data where order doesn't matter.

    - We can combine those sets.

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


print()
print(highschool)
print()
print(middleschool)
print()
print(primaryschool)
print()

friends = highschool.union(middleschool, primaryschool)

print(friends)
