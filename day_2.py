import os


def trapezoid_area(base_up, base_down, height):
    return (base_up + base_down)*height*1/2


area1 = trapezoid_area(height=2, base_down=3, base_up=4)
print area1
area2 = trapezoid_area(2, 3, 4)
print area2


def create_file(filename, msg):
    full_file = os.getcwd() + os.path.sep + filename
    new_file = open(full_file, 'w')
    new_file.write(msg)
    new_file.close()


create_file('test.txt', "3Q666")

for letter in 'heyanyu':
    print letter

if 2 + 2 == 5:
    print "666"
else:
    print "893"

i = 0
while i < 10:
    print i
    i += 1

fruit = [1, 2, 3, 4]
print fruit
fruit.insert(0, 99)
print fruit

print fruit[0:]

people = {"1": "sb", "2": "hxt"}
print people
print "1" in people

people_2 = {1: "666", 1: "5555"}
print people_2


class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print ('You got {} cal energy!').format(self.calories)




cola = CocaCola('tets')
cola.drink()

