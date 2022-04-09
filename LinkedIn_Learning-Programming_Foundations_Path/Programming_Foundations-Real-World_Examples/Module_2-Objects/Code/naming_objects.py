class shirt:
    def __init__(self):
        self.clean = True
    
    def make_dirty(self):
        self.clean = False
    
    def make_clean(self):
        self.clean = True


red_shirt = shirt()
green_shirt = red_shirt
gray_shirt = shirt()

print('red_shirt is: {}'.format(red_shirt.clean))
print('green_shirt is: {}'.format(green_shirt.clean))

red_shirt.make_dirty()

print('red_shirt is: {}'.format(red_shirt.clean))
print('green_shirt is: {}'.format(green_shirt.clean))

green_shirt.make_clean()

print('red_shirt is: {}'.format(red_shirt.clean))
print('green_shirt is: {}'.format(green_shirt.clean))


print('gray_shirt is: {}'.format(gray_shirt.clean))
gray_shirt.make_dirty()
print('gray_shirt is: {}'.format(gray_shirt.clean))

gray_shirt.make_clean()
print('gray_shirt is: {}'.format(gray_shirt.clean))


print(id(red_shirt))
print(id(green_shirt))
print(id(gray_shirt))

