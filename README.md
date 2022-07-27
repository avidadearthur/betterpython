# Write Better Python Code

This repository contains the code examples used in my Write Better Python Code series published on YouTube:

https://www.youtube.com/playlist?list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N

## 1 - coupling and cohesion
### Introduction
...
### What is cohesion?
...
### What is coupling?
...
### Code example intro
...
### Analyzing the code
...
### Information expert
...
### Reducing coupling
...
### Improving cohesion
...

## 2 - dependency inversion
Dependecy inversion helps you write code that can be more easily reusable. A key ingredient of dependecy inversion is abstraction:
it separates the description of an interface from the actual implementation.
### Creating an abstract class in Python
Python doesn't have interfaces built into the sintax but we can use a module called ABC (Abstract Base Class) that allows programmers to use dependecy inversion.
### Making a subclass
This code example is centered around removing the dependency of LightBulb on the PowerSwitch class. To do so, we create an abstract class that acts as a blueprint of how switchable classes should behave (what methods they should implement).
### Modifying the power switch class & Adding another switchable subclass
The next thing we do in the example is to replace the argument in the ElectricPowerSwitch to any implementation of the Switchable Interface rather than a LightBulb instance. 
Now, if we create another implementation of the Switchable Interface such as the Fan class, we can pass it to ElectricPowerSwitch without having to make any changes to this class.

## 3 - strategy pattern
In computer programming, the strategy pattern is a behavioral software design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.[[1]](https://en.wikipedia.org/wiki/Strategy_pattern)
### Main problem with the code
...
### Switching to a strategy pattern
...
### Creating concrete strategies
...
### Updating the process_tickets method
...
### Adding a new strategy
...
### A functional version of the strategy
...
### Adding a function type hint