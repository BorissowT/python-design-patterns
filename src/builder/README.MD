 ## Builder design pattern
 
The Builder Pattern is a creation pattern whose intent is to separate the
construction of a complex object from its representation so that you can use
the same construction process to create different representations.
The Builder pattern tries ti solve:

How can a class create different representations of a complex object?
How can a class that includes creating a complex object be simplified?

The Builder and Factory patterns are very similar in the fact that they both
instantiate objects. The main difference between a Builder and a Factory is
when the process of creating the object is very complex, so rather than the 
Factory returning a new instance of ObjectA, it calls the builder director
constructor method Object.construct() that goes through a more complex 
construction process involving several steps. Both return an Object/Product.

Terminology:
Product: The product being built.
Builder: Builds the concrete product. Implements the IBuilder interface.
Builder Interface: The Interface that the Concrete builder should implement.
Director: The class that is responsible for calling the construct() method of product.

This pattern helps to organize initialisation of complex objects.
 We just use a builder to initialise a combination and director to keep all 
 builders in one place.