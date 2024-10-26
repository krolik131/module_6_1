class Animal():
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(self.name + ' съел ' + food.name)
        else:
            print(self.name + ' не стал есть ' + food.name)
            self.alive = False

class Plant():
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
   pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name

wolfe = Predator('Волк с Уолл-Стрит')
dog = Mammal('Хатико')
cvetik = Flower('Цветик семицветик')
apelsin = Fruit('Заводной апельсин')

print(wolfe.name)
print(cvetik.name)

print(wolfe.alive)
print(dog.fed)
wolfe.eat(cvetik)
dog.eat(apelsin)
print(wolfe.alive)
print(dog.fed)
