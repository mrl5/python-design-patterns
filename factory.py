# -*- coding: utf-8 -*-


from classes.cat import Cat
from classes.dog import Dog


def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())