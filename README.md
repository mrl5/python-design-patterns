# Python: Design Patterns
Examples from [Python: Design Patterns] by [Jungwoo Ryoo]

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
3.	[x] [Singleton] - provides global variable object
    - allows for only one instance of a class
    - keeping an information cache: no need to retrieve information from original source every time when it's needed
4.	[x] [Builder] - solution for building complex object
    - doesn't rely on polymorphism (**unlike factory and abstract factory**)
    - example: before building a car, car parts (e.g. tyres, engine, etc.) need to be build and assembled
5.	[x] [Prototype] - clones object according to a prototypical instance
    - problem: creating many identical objects individually could be "expensive"
    - alternative: cloning instead of creation
    - create prototype once, clone it every time when needed

[Factory]: factory.py
[Abstract factory]: abstract_factory.py
[Singleton]: singleton.py
[Builder]: builder.py
[Prototype]: prototype.py

## Structural Patterns
1.	[x] [Decorator] - adds additional feature to the existing object dynamically without using subclassing
2.	[x] [Proxy] - helps with creating an object which is resource intensive
3.	[x] [Adapter] - converts the interface of the class into another one
    - e.g. unifies method names
4.	[x] [Composite] - compose objects into tree structures to represent part-whole hierarchies
    - e.g. menu(submenu1, submenu2) - submenu1(sub11_submenu1, sub12_submenu1) - ...
5.	[ ] Bridge

[Decorator]: decorator.py
[Proxy]: proxy.py
[Adapter]: adapter.py
[Composite]: composite.py
[Bridge]: bridge.py

## Behavioral Patterns
1.	[ ] Observer
2.	[ ] Visitor
3.	[ ] Iterator
4.	[ ] Strategy
5.	[ ] Chain of responsibility

# See also
- [The Little Book of Python Anti-Patterns] by [@QuantifiedCode]
- [The Hitchhiker's Guide to Python] by [@realpython]
- [Dive Into Python 3] by [Mark Pilgrim]

[Python: Design Patterns]: https://www.linkedin.com/learning/python-design-patterns
[Jungwoo Ryoo]: https://www.linkedin.com/learning/instructors/jungwoo-ryoo

[The Little Book of Python Anti-Patterns]: https://docs.quantifiedcode.com/python-anti-patterns/index.html
[@QuantifiedCode]: https://github.com/quantifiedcode

[The Hitchhiker's Guide to Python]: https://docs.python-guide.org/
[@realpython]: https://github.com/realpython

[Dive Into Python 3]: http://www.diveintopython3.net/
[Mark Pilgrim]: https://github.com/diveintomark
