Python OOP Assignment
Q1. What is the purpose of Python's OOP?
Ans. The purpose of Python's Object-Oriented Programming (OOP) is to provide a way to structure and organize code in a modular and reusable manner. OOP allows us to define classes, which are templates or blueprints for creating objects. Objects are instances of classes that encapsulate data (attributes) and behavior (methods). OOP promotes concepts such as encapsulation, inheritance, and polymorphism, which help in writing efficient, scalable, and maintainable code. It allows for code reusability, modularity, and provides a higher level of abstraction, making it easier to manage and understand complex systems.

Q2. Where does an inheritance search look for an attribute?
Ans: In Python, during an inheritance search for an attribute, the search starts with the instance object itself. If the attribute is not found in the instance object, the search continues in the class of the instance object. If the attribute is still not found in the class, the search proceeds to the superclass or base class. This process continues up the inheritance hierarchy until the attribute is found or the search reaches the top-most superclass (typically the object class) without finding the attribute. If the attribute is not found at any level, a AttributeError is raised.

Q3. How do you distinguish between a class object and an instance object?
Ans: In Python, a class object and an instance object are distinguished based on their respective roles and usage.

Class Object: A class object is an object that represents a class itself. It is created when the class definition is executed and is used to define the structure and behavior of instances. Class objects can be used to access class-level attributes and methods but do not contain instance-specific data.

Instance Object: An instance object is an object that is created from a class. It represents a specific instance or occurrence of the class. Each instance has its own unique data (attributes) and can invoke methods defined in the class. Instances are created using the class as a blueprint and can have different attribute values than other instances of the same class.

In summary, the class object is the blueprint or template for creating instance objects, while instance objects are specific instances of the class with their own unique attribute values.

Q4. What makes the first argument in a class’s method function special?
Ans.In Python, the first argument in a class's method function is conventionally named self. It is a reference to the instance of the class on which the method is invoked. It allows the method to access and manipulate the instance's attributes and other methods.

By convention, the first parameter in a method function is named self, although it can technically be named anything. However, it is strongly recommended to use self to maintain consistency and improve code readability.

The self parameter allows us to refer to the instance object within the method. It is automatically passed when the method is called on an instance, and it allows us to access and modify the instance's attributes, invoke other methods of the instance, or perform any other operations specific to that instance.

Note that the use of self as the first argument is a convention in Python, but it is not a keyword. Other languages may use different names or keywords for this purpose, such as this in C++.

Q5. What is the purpose of the init method?
Ans: The __init__ method is a special method in Python classes that is used for initializing objects. It is also known as the constructor method. The primary purpose of the __init__ method is to set the initial state or attributes of an object when it is created from a class.

The __init__ method is called automatically when a new instance of the class is created. It takes the instance itself (conventionally named self) as the first argument, followed by any additional arguments that you want to pass during object creation. Inside the __init__ method, you can define and assign values to the instance variables (attributes) of the object.

The __init__ method allows you to initialize the state of an object by providing default or initial values for its attributes. It allows you to perform any necessary setup or configuration that is required before the object is ready to be used.

Q6. What is the process for creating a class instance?
Ans: The process for creating a class instance involves the following steps:

Define the class: Start by defining the class using the class keyword, followed by the class name and a colon. Inside the class, define attributes and methods that will be associated with instances of the class.

Instantiate the class: To create an instance (object) of the class, use the class name followed by parentheses () like a function call. This will invoke the class's constructor method (__init__) and create a new instance of the class.

Assign the instance to a variable: Capture the created instance by assigning it to a variable. This variable can be used to access the instance's attributes and methods.

Here's an example:

class MyClass:
    def __init__(self, arg1, arg2):
        self.attr1 = arg1
        self.attr2 = arg2

# Instantiate the class
my_instance = MyClass(arg1_value, arg2_value)

# Access instance attributes
print(my_instance.attr1)
print(my_instance.attr2)

# Call instance methods
my_instance.method()

Q7. What is the process for creating a class?
Ans: The process for creating a class in Python involves the following steps:

Use the class keyword: Start by using the class keyword, followed by the name you want to give to the class. The class name should follow the naming conventions for variables (e.g., start with a letter or underscore, followed by letters, digits, or underscores).

Define the class attributes and methods: Inside the class block, define the attributes (data) and methods (functions) that will be associated with instances of the class. These attributes and methods describe the behavior and characteristics of the objects that will be created from the class.

Create instances of the class: After defining the class, you can create instances (objects) of the class using the class name followed by parentheses () like a function call. This will invoke the class's constructor method (__init__) and create a new instance of the class.

Here's an example:

# Define a class
class MyClass:
    class_attribute = "Hello"

    def __init__(self, arg):
        self.instance_attribute = arg

    def instance_method(self):
        print("Instance method called.")

# Create an instance of the class
my_instance = MyClass("World")

# Access class attribute
print(MyClass.class_attribute)

# Access instance attribute
print(my_instance.instance_attribute)

# Call instance method
my_instance.instance_method()

Q8. How would you define the superclasses of a class?
Ans: In Python, you can define the superclasses of a class by specifying them in the parentheses after the class name when defining the class. This is known as class inheritance or subclassing. The superclass, also called the parent class or base class, is the class from which the current class inherits attributes and methods.

Here's the syntax for defining a class with superclasses:

class ChildClass(Superclass1, Superclass2, ...):
    # Class definition
    pass

Q9. What is the relationship between classes and modules?
Ans: In Python, a module is a file containing Python code that can define functions, classes, and variables. A class, on the other hand, is a construct within a module that defines a blueprint for creating objects with specific attributes and behavior.

The relationship between classes and modules is that a module can contain one or more class definitions. Classes can be defined within a module to organize and encapsulate related functionality. The module serves as a container for the classes and provides a way to group related code together.

Classes defined in a module can be imported and used in other modules or scripts by importing the module itself. This allows for code reusability and modular design. Classes can also inherit from classes defined in other modules, creating a hierarchical relationship between modules and classes.

Q10. How do you make instances and classes?
Ans: To make instances and classes in Python, you follow these steps:

Define a class: Use the class keyword to define a class. Inside the class, you define attributes and methods that describe the behavior and characteristics of the objects that will be created from the class.

Create instances: To create an instance (object) of a class, you use the class name followed by parentheses () like a function call. This invokes the class's constructor method (__init__) and creates a new instance of the class.

Access instance attributes and methods: Once you have an instance of a class, you can access its attributes and methods using dot notation (instance.attribute or instance.method()).

Define class attributes: Class attributes are defined inside the class block but outside any methods. These attributes are shared among all instances of the class and can be accessed using the class name or any instance of the class.

Here's an example:

# Define a class
class MyClass:
    class_attribute = "Hello"  # Class attribute shared by all instances

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def instance_method(self):
        print("Instance method called.")

# Create instances of the class
my_instance1 = MyClass("World1")
my_instance2 = MyClass("World2")

# Access instance attributes
print(my_instance1.instance_attribute)
print(my_instance2.instance_attribute)

# Access class attribute
print(MyClass.class_attribute)

# Call instance methods
my_instance1.instance_method()
my_instance2.instance_method()

Q11. Where and how should be class attributes created?
Ans: Class attributes in Python should be created inside the class block but outside any methods. They are defined directly beneath the class declaration, typically following the class docstring if one is present.

Here's an example:

class MyClass:
    class_attribute = "Hello"  # Class attribute

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def instance_method(self):
        print("Instance method called.")
In the above code, class_attribute is a class attribute that is shared among all instances of the class MyClass. It is created inside the class block but outside any methods.

Class attributes are accessed using the class name or any instance of the class. They provide default values or shared data that can be used by all instances of the class.

Q12. Where and how are instance attributes created?
Ans: Instance attributes in Python are created within the methods of a class, typically inside the constructor method (__init__). They are assigned to the instance using the self parameter, which refers to the instance being created.

Here's an example:

class MyClass:
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute  # Instance attribute

    def instance_method(self):
        print("Instance method called.")
In the above code, instance_attribute is an instance attribute that is specific to each instance of the class MyClass. It is created and assigned within the __init__ method using the self parameter.

Instance attributes are accessed and used by individual instances of the class. Each instance can have its own unique values for instance attributes.

Q13. What does the term "self" in a Python class mean?
Ans: In Python, the term "self" is a convention used to refer to the instance of a class within the class's methods. It acts as a reference to the instance itself.

When defining methods in a class, the first parameter is conventionally named self, although you can use any valid variable name. This parameter allows you to access the instance's attributes and methods within the class's methods.

For example, in the following code snippet:

class MyClass:
    def my_method(self):
        print(self.attribute)

my_instance = MyClass()
my_instance.my_method()

Q14. How does a Python class handle operator overloading?
Ans: Python classes can handle operator overloading by defining special methods (also called magic methods or dunder methods) that correspond to specific operators. These special methods allow objects of a class to behave like built-in types and support operations such as addition, subtraction, comparison, and more.

For example, to enable addition between two instances of a custom class, you can define the __add__ method within the class. This method will be called when the + operator is used with instances of the class.

Here's an example:

class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

# Create instances
obj1 = MyClass(5)
obj2 = MyClass(10)

# Use the '+' operator
result = obj1 + obj2
print(result)  # Output: 15

Q15. When do you consider allowing operator overloading of your classes?
Ans: Operator overloading can be considered when you want to define custom behavior for operators on objects of your custom class. It allows you to make your class instances behave like built-in types and perform operations that are meaningful for your class's context.

Here are some scenarios where allowing operator overloading may be useful:

Enhanced functionality: Operator overloading can provide a more intuitive and expressive way of interacting with your objects. For example, if you have a Vector class, you can define the + operator to perform vector addition, making it easier to work with vectors.

Code readability: By defining operator overloading, you can make your code more readable and concise. It allows you to write code that closely resembles the mathematical or logical operations you are performing.

Integration with existing libraries: If your class needs to integrate with existing libraries or frameworks that rely on standard operators, implementing operator overloading allows your class to seamlessly work with those libraries.

However, it's important to use operator overloading judiciously and maintain consistency with the behavior of the operators in the context of your class. Overloading operators should follow established conventions and provide clear and expected behavior.

Q16. What is the most popular form of operator overloading?
Ans: In Python, the most popular form of operator overloading is the arithmetic operator overloading, which includes operators like +, -, *, /, //, %, and others. These operators are commonly overloaded to perform custom mathematical operations on objects of custom classes.

For example, a Vector class can overload the + operator to perform vector addition, the - operator to perform vector subtraction, and so on.

Arithmetic operator overloading allows you to define how mathematical operations should be performed on objects of your class, enabling you to work with instances of your class in a more intuitive and natural way.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Ans: The two most important concepts to grasp in order to comprehend Python OOP code are:

Classes: Classes are the fundamental building blocks of object-oriented programming in Python. A class is a blueprint that defines the attributes (data) and methods (functions) that objects of the class will have. Understanding how classes are defined, how they encapsulate behavior and data, and how instances of classes are created is crucial in comprehending OOP code.

Objects and Instances: Objects are instances of a class. When you create an instance of a class, you are creating an object that has its own unique set of attributes and can perform operations defined by the class's methods. Understanding how objects are created, how they interact with each other, and how they can be manipulated using class methods and attributes is key to comprehending OOP code.

By understanding the concepts of classes and objects, you can navigate and understand OOP code, including how classes are defined, how instances are created, and how objects interact with each other.

Q18. Describe three applications for exception processing.
Ans: Here are three applications for exception processing:

Error handling: Exception processing is commonly used to handle and manage errors that occur during program execution. It allows you to catch and handle specific types of exceptions, providing alternative paths or actions when errors occur. By handling exceptions, you can prevent program crashes and provide informative error messages to users.

Resource management: Exception processing is useful for ensuring proper resource management and cleanup. For example, when working with files, network connections, or database connections, exceptions can be caught to ensure that resources are properly released and cleaned up, even if an error occurs during the process.

Program flow control: Exceptions can be used to control the flow of a program. By raising and catching exceptions at specific points, you can alter the execution path of the program based on certain conditions or events. This can be helpful for implementing control structures or handling specific scenarios in your program logic.

Q19. What happens if you don't do something extra to treat an exception?
Ans: If an exception occurs during program execution and it is not explicitly handled or treated, it will result in an unhandled exception. In such cases, the default behavior is for the program to terminate and an error message (known as a traceback) is displayed, indicating the type of exception, the location where it occurred, and the sequence of function calls leading to the exception.

This abrupt termination of the program can cause data loss, inconsistent program state, and an unsatisfactory user experience. Therefore, it is important to handle exceptions appropriately to ensure that errors are properly managed and the program can recover or gracefully exit when necessary.

Q20. What are your options for recovering from an exception in your script?
Ans: When an exception occurs in your script, you have several options for recovering from it:

Catch and handle the exception: You can use a try-except block to catch and handle specific exceptions. Inside the try block, you place the code that may raise an exception. In the except block, you specify the type of exception you want to handle, and you can provide code to handle the exception, log the error, provide an alternative action, or display an appropriate error message. By catching and handling exceptions, you can control the flow of the program and continue its execution even if an error occurs.

Rethrow the exception: Sometimes, you may want to catch an exception, perform some actions, and then re-raise the exception to be handled at a higher level. This allows you to handle specific exceptions at a local level while still propagating the exception to an outer scope for further handling or logging.

Graceful exit: In some cases, when an exception occurs and there is no way to recover or continue the program execution, you may choose to gracefully exit the script. This can involve cleaning up resources, saving any necessary data, and displaying an appropriate error message to the user before terminating the program.

The appropriate recovery option depends on the nature of the exception, the desired behavior of your script, and the specific requirements of your application.

Q21. Describe two methods for triggering exceptions in your script.
Ans: Here are two methods for triggering exceptions in your script:

Exception raising: You can explicitly raise exceptions using the raise statement. By raising an exception, you indicate that a specific error or condition has occurred at a particular point in your code. You can raise built-in exceptions or create custom exceptions by defining your own exception classes. For example:

raise ValueError("Invalid input. Please enter a positive number.")

Built-in exception triggers: Python provides built-in mechanisms that can automatically trigger exceptions in certain situations. For example, if you attempt to divide a number by zero (0), a ZeroDivisionError exception will be raised automatically. Similarly, if you try to access an index that is out of range in a list or string, an IndexError exception will be raised. These exceptions are triggered by the interpreter based on specific rules and conditions defined in the Python language.

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of
whether or not an exception exists.
Ans: Two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists, are:

Using the finally block: The finally block is a construct used in exception handling that allows you to specify a set of statements that will be executed regardless of whether an exception occurs or not. The statements in the finally block will be executed after the try block and any associated except blocks, regardless of whether an exception was raised or caught. This is useful for performing cleanup operations or releasing resources that need to be executed regardless of the outcome. For example:

try:
    # Code that may raise an exception
    ...
except SomeException:
    # Exception handling
    ...
finally:
    # Cleanup or resource release operations
    ...
Using the atexit module: The atexit module provides a way to register functions to be called at program termination. The functions registered using atexit.register() will be called when the program exits, whether normally or due to an unhandled exception. This is useful for performing final cleanup or closing open resources when the program finishes execution. For example:

def cleanup():
    # Cleanup or resource release operations
    ...

atexit.register(cleanup)

Q23. What is the purpose of the try statement?
Ans: The purpose of the try statement in Python is to define a block of code in which exceptions may occur. The try block is followed by one or more except blocks and optionally a finally block.

The try block is used to enclose the code that may raise exceptions. If an exception occurs within the try block, the code execution within the try block is interrupted, and the corresponding except block(s) are evaluated to determine if they can handle the specific exception raised. If an appropriate except block is found, the code inside that block is executed to handle the exception. If no suitable except block is found, the exception propagates to the outer scope.

The purpose of the try statement is to provide a structured way to handle exceptions and allow for graceful error handling and recovery within your code.

Q24. What are the two most popular try statement variations?
Ans: The two most popular try statement variations are:

try-except statement: The try-except statement is used to catch and handle specific exceptions that may occur within the try block. It allows you to specify one or more except blocks that handle different types of exceptions. When an exception occurs in the try block, the corresponding except block(s) are evaluated to determine if they can handle the specific exception. This variation provides a structured way to handle exceptions and gracefully recover from errors.

try-finally statement: The try-finally statement is used to define a finally block that will be executed regardless of whether an exception occurs or not. The finally block is executed after the try block and any associated except blocks, even if an exception was raised and caught. This variation is useful for performing cleanup operations or releasing resources that need to be executed regardless of the outcome, ensuring that certain actions are always performed.

Q25. What is the purpose of the raise statement?
Ans: The raise statement in Python is used to explicitly raise an exception. It allows you to trigger and propagate exceptions manually in your code. The purpose of the raise statement is to indicate that a specific error or condition has occurred at a particular point in your code. You can raise built-in exceptions or create custom exceptions by defining your own exception classes. The raise statement is typically followed by an exception object or an exception class, which represents the type of exception being raised. You can also provide an optional error message to provide additional information about the exception. The raise statement allows you to control the flow of your program and handle exceptional situations according to your requirements.

Q26. What does the assert statement do, and what other statement is it like?
Ans: The assert statement in Python is used as a debugging aid to test if a certain condition is true. It takes a condition as an argument and raises an AssertionError exception if the condition is false. The purpose of the assert statement is to assert that certain conditions must be true at certain points in the code. It is often used to check assumptions and detect logical errors during development and debugging.

The assert statement is similar to the if statement in terms of evaluating a condition. However, unlike the if statement, the assert statement is used specifically for debugging purposes and is typically removed or disabled in production code. It allows developers to express their expectations and assumptions about the code, helping to catch and identify errors early in the development process.

Q27. What is the purpose of the with/as argument, and what other statement is it like?
Ans: The with/as statement in Python is used for context management. It provides a convenient way to ensure that resources are properly managed and cleaned up after usage, even in the presence of exceptions. The purpose of the with/as statement is to simplify the management of resources, such as file operations or acquiring and releasing locks.

The with/as statement is used in combination with objects that implement the context management protocol, which requires the objects to define __enter__() and __exit__() methods. The __enter__() method is called when the with block is entered, allowing the setup of resources, and the __exit__() method is called when the with block is exited, allowing the cleanup of resources.

Q28. What are *args, **kwargs?
Ans: *args and **kwargs are special syntax in Python used to pass a variable number of arguments to a function.

*args is used to pass a variable number of positional arguments to a function. It allows you to pass any number of arguments, separated by commas, to a function. Inside the function, the *args parameter becomes a tuple containing all the passed arguments. You can iterate over the args tuple or access individual arguments by indexing.

Example:

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
Output:

1
2
3
**kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass key-value pairs as arguments to a function. Inside the function, the **kwargs parameter becomes a dictionary containing the passed keyword arguments. You can access the values using the keys or iterate over the items in the dictionary.

Example:

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='John', age=25, city='London')
Output:

name John
age 25
city London

Q29. How can I pass optional or keyword parameters from one function to another?
Ans: To pass optional or keyword parameters from one function to another, you can use the *args and **kwargs syntax along with the unpacking operator (*) when calling the function.

Here's an example:

def foo(a, b, c=0):
    print(a, b, c)

def bar(*args, **kwargs):
    foo(*args, **kwargs)

bar(1, 2, c=3)
In the above example, the function foo() has parameters a, b, and an optional parameter c with a default value of 0. The function bar() accepts *args and **kwargs to collect any number of positional and keyword arguments.

By using foo(*args, **kwargs) inside bar(), the arguments passed to bar() are unpacked and forwarded to foo(), allowing the optional or keyword parameters to be passed along. In this case, 1 and 2 are assigned to a and b in foo(), and c=3 is passed as a keyword argument.

Q30. What are Lambda Functions?
Ans: Lambda functions, also known as anonymous functions, are small, inline functions in Python that don't require a separate function definition using the def keyword. They are defined using the lambda keyword and can take any number of arguments but can only have a single expression.

Lambda functions are often used in situations where a small function is needed for a short period of time and doesn't require a full function definition. They are commonly used with built-in functions like map(), filter(), and reduce(), or in scenarios where a function needs to be passed as an argument to another function.

Here's an example of a lambda function:

multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)  # Output: 12

Q31. Explain Inheritance in Python with an example?
Ans: Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and behaviors from another class. It enables code reuse and the creation of hierarchical relationships between classes.

In Python, a class can inherit from one or more parent classes, known as superclasses or base classes, by specifying them in parentheses after the class name. The class that inherits from another class is called a subclass or derived class.

Here's an example to illustrate inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.sound())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.name)  # Output: Whiskers
print(cat.sound())  # Output: Meow!

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
Ans: When a class C inherits from multiple classes A and B, and both A and B have their own versions of a method func(), the version of func() that gets invoked depends on the method resolution order (MRO).

In Python, the MRO is determined by the C3 linearization algorithm, which follows a depth-first left-to-right traversal of the inheritance hierarchy. The MRO ensures that the method lookup order is consistent and avoids the diamond inheritance problem.

In the case of class C(A, B), the MRO is determined by the order of classes specified in the inheritance declaration. The method resolution order can be accessed using the __mro__ attribute of the class.

For example:

class A:
    def func(self):
        return "A"

class B:
    def func(self):
        return "B"

class C(A, B):
    pass

obj = C()
print(obj.func())  # Output: A

Q33. Which methods/functions do we use to determine the type of instance and inheritance?
Ans: In Python, we can use the following methods/functions to determine the type of an instance and inheritance:

type(): The type() function returns the type of an object. It can be used to determine the type of an instance or object.

Example:

x = 5
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>

z = [1, 2, 3]
print(type(z))  # Output: <class 'list'>

class MyClass:
    pass

obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>

isinstance(): The isinstance() function is used to check if an object is an instance of a particular class or any of its subclasses. It returns True if the object is an instance of the specified class or its subclasses; otherwise, it returns False.

Example:

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car()
print(isinstance(car, Car))  # Output: True
print(isinstance(car, Vehicle))  # Output: True
print(isinstance(car, Motorcycle))  # Output: False

issubclass(): The issubclass() function is used to check if a class is a subclass of another class. It returns True if the class is a subclass of the specified class; otherwise, it returns False.

Example:

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

print(issubclass(Car, Vehicle))  # Output: True
print(issubclass(Motorcycle, Vehicle))  # Output: True
print(issubclass(Car, Motorcycle))  # Output: False

Q34.Explain the use of the 'nonlocal' keyword in Python.
Ans: In Python, the nonlocal keyword is used to declare a variable in a nested function as non-local, i.e., it refers to a variable in the nearest enclosing scope that is not global. It allows the nested function to assign a value to a variable in its enclosing scope, rather than creating a new local variable with the same name.

The nonlocal keyword is used when we have a nested function inside another function, and we want to modify a variable from the enclosing scope in the nested function.

Here's an example to illustrate the use of the nonlocal keyword:

def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
        print("Inner:", x)
    
    inner_function()
    print("Outer:", x)

outer_function()
Output:

Inner: 15
Outer: 15

Q35. What is the global keyword?
The global keyword in Python is used to indicate that a variable is a global variable, meaning it is defined in the global scope and can be accessed and modified from anywhere within the program, including inside functions or classes.

When you use the global keyword before a variable name within a function or class method, it informs Python that the variable being referenced is the global variable with the same name, rather than creating a new local variable with that name.

Here's an example to demonstrate the use of the global keyword:

x = 10  # global variable

def modify_global():
    global x
    x += 5
    print("Inside function:", x)

print("Before function call:", x)
modify_global()
print("After function call:", x)
Output:

Before function call: 10
Inside function: 15
After function call: 15