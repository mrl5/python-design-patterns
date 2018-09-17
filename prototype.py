# -*- coding: utf-8 -*-

import copy
from classes.car import Car


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


c = Car()
c.model = "Skylark"
c.tires = "Runflat tires"
c.engine = "Bi-Turbo engine"

prototype = Prototype()
prototype.register_object('skylark', c)

c1 = prototype.clone('skylark')

print(c1)
