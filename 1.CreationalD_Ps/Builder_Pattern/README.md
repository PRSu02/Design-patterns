# Builder Pattern

## Intent
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

## Explanation
Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scattered all over the client code.

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called builders.

## Structure
- **Product**: The complex object that is being built.
- **Builder**: Abstract interface for creating parts of a Product object.
- **ConcreteBuilder**: Constructs and assembles parts of the product by implementing the Builder interface.
- **Director**: Constructs an object using the Builder interface.

## Running the Example
```bash
python main.py
```
