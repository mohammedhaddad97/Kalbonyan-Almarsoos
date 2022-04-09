cities = ['Cairo', 'Giza', 'Alexandria']
streets = [
    ['Al-Moezz', 'Bein-Alqasrein', 'Al-Azhar'],
    ['Al-Haram', 'King-Faisal', 'Highdam'],
    ['Al-Agamy', 'Sidi Gaber', 'Sidi Bishr']
]

buildings = [
    [
        ['Cairo, Moez, B1', 'Cairo, Moez, B2', 'Cairo, Moez, B3'],
        ['Cairo, Alqasrein, B1', 'Cairo, Alqasrein, B2', 'Cairo, Alqasrein, B3', 'Cairo, Alqasrein, B4'],
        ['Cairo, Azhar, B2', 'Cairo, Azhar, B2']
        
    ],
    [
        ['Giza, Haram, A1', 'Giza, Haram, A2'],
        ['Giza, Faisal, A1', 'Giza, Faisal, A2', 'Giza, Faisal, A3'],
        ['Giza, Azhar, A1']
    ],
    [
        ['Alex, Agamy, C1', 'Alex, Agamy, C2'],
        ['Alex, Gaber, C1', 'Alex, Gaber, C2', 'Alex, Gaber, C3'],
        ['Alex, Bishr, C1', 'Alex, Bishr, C2', 'Alex, Bishr, C3']
    ]
]


'''
    Task:
         1- Print out cities.
         2- Print out streets.
         3- Print out buildings.
'''
# Task 1: Print out cities.
print()
print('Cities in Egypt:')
for city in cities:
    print(city)

print('++++++')

# Task 2: Print out streets.
print()
print('Streets in Egypt:')
for city in streets:
    for street in city:
        print(street)


print('++++++')

# Task 3: Print out buildings.
print()
print('Buildings in Egypt:')

for city in streets:
    for city in buildings:
        for street in city:
            for building in street:
                print(building)