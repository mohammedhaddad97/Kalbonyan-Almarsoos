from xml.etree.ElementTree import tostringlist


def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it..')
    print('Cooking the other side')

def make_omelette(ingredient):
    mix_and_cook()
    return 'a {} omelette'.format(ingredient)

def make_pancake():
    mix_and_cook()
    print('a tasty pancake')

def fancy_omelette(*ingredients):
    mix_and_cook()
    return 'a {} ingredient omelette'.format(len(ingredients))

print(make_omelette('Cheese'))

print()
print('+++++++++++++++')
print()

print(fancy_omelette('onion', 'cheese', 'garlic', 'pepper', 'tomatoe', 'salt', 'mushroom'))
