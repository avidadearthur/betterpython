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
The method that process tickets is very long and has weak cohesion. In the Strategy design pattern we'll solve this issue with an abstract base class that can be implemented in different ways depending on the chosen strategy.
### Switching to a strategy pattern
We start by creating a strategy Interface using the ABC (Abstract Base Class) module - see "2 - dependency inversion" for more details. This interface can have as many child classes as needed, each representing a different strategy.
### Creating concrete strategies and Updating the process_tickets method
The strategies come in the form of three class implementations: Fifo, Lifo and Random ordering of tickets.

Then we updated the process_tickets method from the CostumerSupport class. Rather than 'processing_strategy' being a str that defines the path the program will take in an If-Else block, it becomes a TicketOrderingStrategy implementation. That way the ordering work is left for the iplementations and not for the Costumer Support class.
### A functional version of the strategy
A simpler way to achieve the same improvement in cohesion does not involve abstract classes. In python you can symply use the functions and pass them as arguents.

To be more clear Arjan imports the 'Callable' keyword and adds the type hint: <code>ordering: Callable[[List[SupportTicket]], List[SupportTicket]]<code>.

## 3 - Strategy Pattern

### Explaining the code example

### Analysis

### Creating a simple event handler

### Moving to an event-based approach

### The complete solution
### The power of an event-based system
