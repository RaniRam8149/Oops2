Q5. Can we create an instance of an abstract class? Explain your answer.

In Python, you cannot directly create an instance of an abstract class. Attempting to instantiate an abstract class will result in an error.

Abstract classes are meant to be templates or blueprints for other classes to inherit from. They typically contain abstract methods that lack implementation and are meant to be overridden by subclasses. These abstract methods act as placeholders, defining a structure that subclasses must follow.

Python's abc module provides the ABC class and the abstractmethod decorator, which allow the creation of abstract classes and abstract methods, respectively. When a class contains at least one abstract method, it becomes an abstract class, and Python prevents you from creating instances of such classes.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2

shape = Shape() 
