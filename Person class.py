class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = None

    def __str__(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}')

    def add_dog(self, dog):
        if isinstance(dog, Dog):
            self.dog = dog
        else:
            raise ValueError

    def bark(self):
        if self.dog:
            self.dog.bark()
        else:
            print(f"{self.name} doesn't have a dog.")


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name}: Woof!')


p1 = Person('Igor', 20, 'male')
dog1 = Dog('Busya')
p1.add_dog(dog1)
p1.bark()
