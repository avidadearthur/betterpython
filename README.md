# Write Better Python Code

This repository contains the code examples used in my Write Better Python Code series published on YouTube:

https://www.youtube.com/playlist?list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N

## 1 - coupling and cohesion
Coupling is the measure of the degree of interdependence between the modules. A good software will have low coupling. Cohesion is a measure of the degree to which the elements of the module are functionally related. It is the degree to which all elements directed towards performing a single task are contained in the component. Basically, cohesion is the internal glue that keeps the module together. A good software design will have high cohesion. [[0]](https://www.geeksforgeeks.org/software-engineering-coupling-and-cohesion/)

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

To be more clear Arjan imports the 'Callable' keyword and adds the type hint: <code>ordering: Callable[[List[SupportTicket]], List[SupportTicket]]</code>.

## 4 - Observer Pattern
The observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

It is mainly used for implementing distributed event handling systems, in "event driven" software. In those systems, the subject is usually named a "stream of events" or "stream source of events", while the observers are called "sinks of events". The stream nomenclature alludes to a physical setup where the observers are physically separated and have no control over the emitted events from the subject/stream-source. This pattern then perfectly suits any process where data arrives from some input that is not available to the CPU at startup, but instead arrives "at random" (HTTP requests, GPIO data, user input from keyboard/mouse/..., distributed databases and blockchains, ...).[[2]](https://en.wikipedia.org/wiki/Observer_pattern)
### Explaining the code example
This example doesn't implement the Observer pattern in the traditional way: Subject notifying observers to react to a certain event. It illustrates a event management system.
Suppose you write a back-end API and you develop a user registry function next to a operations database that sends a message to the sales team, sends a welcome email to the user and writes a log to the server somewhere.
The observer.py file handles the registration of a new user using the API modules plan.py and user.py. These two scripts carry out their tasks by importing the modules from lib, which simulate some database, email, slack, etc... interaction.

### Analysis
The problem with this code is that if, for instance, you look  at register_new_user from user.py you'll find a function with very weak cohesion: it interacts with the DB but also with the email, slack and log functioality. The same problem is found in <code>password_forgotten</code> and <code>upgrade_plan</code>. This is where an event 
### Creating a simple event handler
The event system has a number of subscribers that subscribe for a different number of events and each item in the dictionary will be a list of subscribers that need to be notified every time that event occurs.
The only thing we have to do when we subscribe to an event type is to check if there's already a list of that event type otherwiise we create it.
We also need to be able to post an event and pass some data with it.     If the event doesn't exist, the function doesn't do anything. Otherwise the data will be transmitted for each subscriber function.
### Moving to an event-based approach
Now what we can do is to go back to the user functions and replace the old code with post_event calls. This helps to group different event handlers in a way that makes sense instead of leaving up to the user.py functions to post the events.
### The power of an event-based system
Therefore the only dependency is on the event_handler system. On top of what has been done, we could add log and email listeners. Since user.py simply posts an event, the code is also very flexible to API changes.
## 5 - Unit Testing
Unit testing is a software development process in which the smallest testable parts of an application, called units, are individually and independently scrutinized for proper operation. This testing methodology is done during the development process by the software developers and sometimes QA staff.[[3]](https://www.techtarget.com/searchsoftwarequality/definition/unit-testing)
### Explaining the example
Suppose we have a system that stores information about vehicles. The class vehicle has two methods: one for computing taxes and another that checks if you can lease a car instance.
### Setup unit testing
In the video example we used unittest as a test library and created a different file for the test methods.
Note that all test methods must start with 'test'_ . Moreover you can obtain html reports from the test class.
Refer to the [documentation](https://docs.python.org/3/library/unittest.html) for more details.

## 6 - Template method
The "template method" is implemented as a method in a base class (usually an abstract class). This method contains code for the parts of the overall algorithm that are invariant. The template ensures that the overarching algorithm is always followed. In the template method, portions of the algorithm that may vary are implemented by sending self messages that request the execution of additional helper methods. In the base class, these helper methods are given a default implementation, or none at all (that is, they may be abstract methods).

Subclasses of the base class "fill in" the empty or "variant" parts of the "template" with specific algorithms that vary from one subclass to another. It is important that subclasses do not override the template method itself.
[[4]](https://en.wikipedia.org/wiki/Template_method_pattern)

### Implementing the template method
As a first step we'll aggregate the functions that are allways called during the trading process. This entails creating a trading bot that contains the check prices method and then write abstract methods for the different parts of the check price algorithm.
The class TradingBot is for the most part the same as the Application class. The main difference is at the level of the should_buy and should_sell methods - we'll turn these two functions into abstract method that we can implement diferently according to the trading stratgy you want to follow.

For instance, we can create a AverageTrader class that uses the average of the prices to sell and buy stocks and we can also create a MinMaxTrader that uses the historical minimum and maximum to decide wether to buy or sell stocks.
### Implementing the bridge method
TradingBot, however, still has a problem: it engages in activities that it shouldn't deal with - such as connecting to an exchange or getting market data from an exchange. To solve this we'll use the bridge design pattern: it will let us have an abstraction and its implementation defined and extended independently from each other. Put other way: the Trader can have different exchanges and different tradding strategies but the exchanges and the strategies are decoupled in different class hierachies.

We start by creating an Exchange interface that will allow mutiple coin exchange implementations. Since we define the TradingBot class to receive a generic Exchange implementation, all exchanges added can be used by the different trading startegies. Therefor we improve the degree of coupling of the code.

## 7 - Error Handling