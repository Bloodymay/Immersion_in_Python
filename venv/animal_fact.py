class Animal:
    def __init__(self, name):
        self.name = name





class Bird(Animal):
    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(self.name)

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        self.max_depth = max_depth
        super().__init__(self.name)

    def depth(self):
        if 6000 >= self.max_depth >= 200:
            return "Глубоководная"
        elif 200 > self.max_depth >= 10:
            return "Средневодная"
        elif 0 < self.max_depth < 10:
            return "Мелководная"


class Mammal(Animal):
    def __init__(self, name,weight):
        self.weight = weight
        super().__init__(self.name)

    def category(self):
        if 1000 >= self.weight > 500:
            return "Гигант"
        elif 500 >= self.weight >= 50:
            return "Обычный"
        elif 0 < self.weight < 50:
            return "Малявка"


class AnimalFactory:
    def __init__(self, animal_type, animal_name, param) -> None:
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.param = param

    def create_animal(self, *args):
        animal_classes = {"Bird": Bird, "Fish": Fish, "Mammal": Mammal}
        new_animal = animal_classes[self.animal_type](self.animal_name, self.param)
        type_a = None
        if animal_type == "Bird":
            type_a = new_animal.wing_length()

        elif animal_type == "Fish":
            type_a = new_animal.depth()

        elif animal_type == "Mammal":
            type_a = new_animal.category()



        return f"Класс: {self.animal_type}, Имя: {self.animal_name}, Тип: {type_a}"


animal_type, animal_name, param = input("Введите животное:").split(" ")

a1 = AnimalFactory(animal_type,animal_name,float(param))

print(f"Имя животного- {animal_name}, тип животного - {animal_type}, параметр - {a1.create_animal(param)}")