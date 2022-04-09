def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it..')
    print('Cooking the other side')

def make_omelette():
    mix_and_cook()
    return 'a tasty omelette'

def make_pancake():
    mix_and_cook()
    print('a tasty pancake')

omelette = make_omelette()
print(omelette)

pancake = make_pancake()
print(pancake)