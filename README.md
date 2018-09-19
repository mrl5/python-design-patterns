# Python: Design Patterns
* [ ] Examples from [Python: Design Patterns] by [Jungwoo Ryoo]
* [ ] Examples from [Python: Advanced Design Patterns] by [Jungwoo Ryoo]

## Design Patterns
- Well-known solutions to recurring problems (same problem occurring over and over again)
- Widely accepted solutions by the software development community
- No need to re-invent the wheel

## Creational Patterns
1.	[x] [Factory] - object specializing in creating other objects
    - when not sure what type of object will be needed
    - decisions to be made at runtime regarding what classes to use
2.	[x] [Abstract factory] - creates a factory of related objects without explicitly specifying their classes
    - useful when delivering family of related objects
    - don't need to know which family it is until runtime
    - relations: factory and singleton (concrete factory are often made as it)
3.	[x] [Singleton] - provides global variable object
    - allows for only one instance of a class
    - keeping an information cache: no need to retrieve information from original source every time when it's needed
4.	[x] [Builder] - solution for building complex object
    - doesn't rely on polymorphism (**unlike factory and abstract factory**)
    - example: before building a car, car parts (e.g. tyres, engine, etc.) need to be build and assembled
5.	[x] [Prototype] - clones object according to a prototypical instance
    - problem: creating many identical objects individually could be "expensive"
    - alternative: cloning instead of creation
    - solution: create prototype once, clone it every time when needed
    - relations: abstract factory

[Factory]: factory.py
[Abstract factory]: abstract_factory.py
[Singleton]: singleton.py
[Builder]: builder.py
[Prototype]: prototype.py

## Structural Patterns
1.	[x] [Decorator] - adds additional feature to the existing object dynamically without using subclassing
    - relations: adapter, composite, strategy
2.	[x] [Proxy] - helps with creating an object which is resource intensive
    - relations: adapter, decorator
3.	[x] [Adapter] - converts the interface of the class into another one
    - e.g. unifies method names
    - relations: bridge, decorator
4.	[x] [Composite] - composes objects into tree structures to represent part-whole hierarchies
    - e.g. menu(submenu1, submenu2) - submenu1(sub11_submenu1, sub12_submenu1) - ...
    - relations: decorator, iterator, visitor
5.	[x] [Bridge] - decouples an abstraction from its implementation so that the two can vary independently
    - publish interface in an inheritance hierarchy, and bury implementation in its own inheritance hierarchy
    - relations: abstract factory, adapter

[Decorator]: decorator.py
[Proxy]: proxy.py
[Adapter]: adapter.py
[Composite]: composite.py
[Bridge]: bridge.py

## Behavioral Patterns
1.	[x] [Observer] - establishes an one-to-many relation between a subject and multiple observers
    - problem: subject needs to be monitored, and observers need to be notified on subject's change
    - relations: singleton
2.	[x] [Visitor] - allows adding new features to the existing class hierarchy without changing it
    - can provide operations on a composite objects
3.	[ ] Iterator
4.	[ ] Strategy
5.	[ ] Chain of responsibility

[Observer]: observer.py
[Visitor]: visitor.py
[Iterator]: iterator.py
[Strategy]: strategy.py
[Chain of responsibility]: chain_of_responsibility.py

# See also
- [The Little Book of Python Anti-Patterns] by [@QuantifiedCode]
- [The Hitchhiker's Guide to Python] by [@realpython]
- [Dive Into Python 3] by [Mark Pilgrim]
- [python-patterns] (a collection of design patterns and idioms in Python) by [@faif]
- A [detailed description of design patterns] by [SourceMaking](https://sourcemaking.com/)

[Python: Design Patterns]: https://www.linkedin.com/learning/python-design-patterns
[Python: Advanced Design Patterns]: https://www.linkedin.com/learning/python-advanced-design-patterns
[Jungwoo Ryoo]: https://www.linkedin.com/learning/instructors/jungwoo-ryoo

[The Little Book of Python Anti-Patterns]: https://docs.quantifiedcode.com/python-anti-patterns/index.html
[@QuantifiedCode]: https://github.com/quantifiedcode

[The Hitchhiker's Guide to Python]: https://docs.python-guide.org/
[@realpython]: https://github.com/realpython

[Dive Into Python 3]: http://www.diveintopython3.net/
[Mark Pilgrim]: https://github.com/diveintomark

[detailed description of design patterns]: https://sourcemaking.com/design_patterns/

[python-patterns]: https://github.com/faif/python-patterns
[@faif]: https://github.com/faif
