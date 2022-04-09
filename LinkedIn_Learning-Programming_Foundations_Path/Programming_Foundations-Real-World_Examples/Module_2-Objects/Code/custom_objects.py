class jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True

    def put_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False
            
    def is_pants_on(self):
        if self.wearing == True:
            print('Pants are on')
        else:
            print('Pants are off')

jeans_1 = jeans(30, 57, 'black')

print()

jeans_1.put_on()
jeans_1.is_pants_on()

print('\n+++\n')

jeans_1.put_off()
jeans_1.is_pants_on()