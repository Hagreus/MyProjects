class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f'Dog named {self.name}, breed {self.breed}')


dog1 = Dog('Puziko', 3, 'labrador')
dog1.bark()