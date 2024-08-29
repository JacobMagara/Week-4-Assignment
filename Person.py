class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name}."

    def is_adult(self):
        return self.age >= 18

    def describe(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def introduce(self):
        print(f"Hi, my name is {self.name}. I'm {self.age} years old and I'm {self.gender}.")

person1 = Person ("JohnDoe", 35 , "Male")
person2 = Person ("JaneDoe", 28 , "Female")

person1.introduce()
person2.introduce()