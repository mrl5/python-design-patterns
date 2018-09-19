# -*- coding: utf-8 -*-


class Subject(object):
    """Represents what is being 'observed'"""
    def __init__(self):
        # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers
        self._observers = []

    def attach(self, observer):
        # If the observer is not already in the observers list
        if observer not in self._observers:
            # append the observer to the list
            self._observers.append(observer)

    # Simply remove the observer
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            # Don't notify the observer who is actually updating the temperature
            if modifier != observer:
                # Alert the observers!
                observer.update(self)


class Core(Subject):
    """Inherits from the Subject class"""
    def __init__(self, name=""):
        Subject.__init__(self)
        # Set the name of the core
        self._name = name
        # Initialize the temperature of the core
        self._temp = 0

    @property # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    # Alert method that is invoked when the notify() method in a concrete subject is invoked
    def update(self, subject):
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90

