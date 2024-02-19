Q3. What is abc module in python? Why is it used?

The abc module in Python stands for "Abstract Base Classes." It provides tools for creating abstract base classes and working with them. Abstract base classes are classes that are meant to be subclassed but not instantiated directly. They serve as templates for other classes to inherit from, defining a set of methods or properties that must be implemented by their subclasses.

The main purpose of the abc module is to enforce a certain structure in subclasses by defining abstract methods. This helps in:

1.Providing a Blueprint: Abstract base classes define a common interface that subclasses must adhere to. They act as a blueprint for the expected methods and properties that derived classes should implement.

2.Enforcing Structure: Subclasses that inherit from abstract base classes must implement all the abstract methods defined in the base class. If a subclass fails to do so, it will raise an error, enforcing the implementation of necessary functionality.
