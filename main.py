#+ 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("звук этого животного !!!")
    def eat(self):
        print("ест что-тоо животное !!!")

class Bird(Animal):  # птица
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print("чирик-чирик !!!")

    def eat(self):
        print("птица")
        super(Bird, self).eat()

    def fly(self):
        print(f"{self.name} летает с размахом крыльев {self.wing_span} метров !!!")


class Mammal(Animal):  # млекопитающее
    def __init__(self, name, age, has_a_tail):
        super().__init__(name, age)
        self.has_a_tail = has_a_tail

    def make_sound(self):
        print("рычит !!!")

    def eat(self):
        print("млекопитающее")
        super(Mammal, self).eat()

    def get_has_a_tail(self):
        print(f"У {self.name} есть хвост =  {self.has_a_tail} ")


class Reptile(Animal):  # рептилия
    def __init__(self, name, age, poisonous):
        super().__init__(name, age)
        self.poisonous = poisonous

    def make_sound(self):
        print("шипит !!!")

    def eat(self):
        print("рептилия")
        super(Reptile, self).eat()

    def get_poisonous(self):
        print(f"{self.name} ядовитая =  {self.poisonous} ")





bird = Bird("Воробей", 2, 0.3)
bird.make_sound()  # Вывод: чирик-чирик !!!
bird.eat()         # Вывод: ест что-то животное !!!
bird.fly()         # Вывод: Воробей летает с размахом крыльев 0.3 метров !!!

dog = Mammal("ПесБарбос", 4, 1)
dog.make_sound()
dog.eat()
dog.get_has_a_tail()

pit = Reptile("Питон", 10, 0)
pit.make_sound()
pit.eat()
pit.get_poisonous()
