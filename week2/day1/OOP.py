# ----- Object Oriented Programing ----- #

#  everything in python is an object:
# dictionatries
# lists
# functions
# Variables
# classes

# objects have 2 parts
# Attributes
# What it HAS
# Methods
# What it DOES


# class Person():
#     def __init__(self):
#         self.name = None

# class:       ---- defines new class
# Person():    ---- name of class(PancaleCase)
# def          ---- def
# __           ---- called a dunder(double underscore)
#init         ---- constructor
# (self)       ---- make objects from this class
# .name = None ---- name has no value


class Person():
    def __init__(self, name, age, height, profession,):
        self.name = name
        self.age = age
        self.height = height
        self.profession = profession
        self.hobbies = []

    def set_hair(self, hair):
        self.hair = hair

    def get_hair(self):
        for hair in self.hair:
            print(self.hair)

    def set_hobbies(self, hobby):
        self.hobbies.append(hobby)

    def get_hobbies(self):
        for hobby in self.hobbies:
            print(hobby)


person_1 = Person("James", 24, "5'10''", "Unemployed Trash")

person_2 = Person("Gregg", 1, "8''", "Sausage Roll")

# print(vars(person_1))

# print(person_2.__dict__)
