# Computational thinking
1. Decomposition 
    > We use helper functions to break down a big program to small functions to increase the usability and maintainability.
2. Pattern matching and data representation
    > We use number%2 == 0 to find even numbers in a list of numbers.
3. Abstraction and generalization
    > for loop use abstraction to do iteration
4. Automation with algorithm
    > Use while loop and if statement to ask user input command again and again automatically, until they input 'quit'

# 4 main control structure
1. sequence
   ```python
    number = 1
    number += 1
    print(number)
   ```
2. repetition
   ```python
   for number in range(10):
        print(number)
   ```
3. selection
   ```python
   number = 3
    if number % 2 == 0:
        print('This is even.')
    else:
        print('This is odd')
   ```
4. indirection
   ```python
    def square(number):
        return number * number
    print(square(number))
   ```

# LBYL
* Look before you leap
* Check for precondition before making function calls or execute other operation
    ```python
    if key in dictionary_1:
        dictionary_1[key] += 1
    ```

# EAFP
* easy to ask for forgiven than permission
* You should just start by doing wat you expect to work
    ```python
    try:
        dictionary_1[key] += 1
    except KeyError:
        print('No key')
    else:
        do_other_things()
    ```
# reference
Object address. A variable is bounded to an object. It stores an address, which is also called reference, to the object in memory.

# interning
Python preloads and interns some object when it starts to run a program. For example, integer [-5, 255]

# duck typing
We treat an object by its behavior rather than object type itself.

If an object can be concatenated, indexed, and convert to Unicode, it does everything as a string can do. We treat this object like a string.

# scope
A variable is defined and visible in a part of program. There are 3 kinds of scope: built-in, global, and local scope.

# function and method
We can call a function independently. Methods are special functions associated with object. If we want to use a method, we should use with object and dot syntax, for example dictionary_1.items().

# Types
Type defines the kind of things we can do to this object. For example, we can use + to add two integers. We can also use + to concatenate two strings.

# five tools to error-free code
1. Pair programming
2. Walk through
3. print statement
4. debugger
5. unit test

# 3 difference: dictionary vs. set
1. key-value pairs <-> single elements
2. value can be mutable <-> immutable
3. method keys(), values(), items() <-> add(),union, difference()

# variable length parameter vs arbitrary keyword arguments
1. *args <-> **kwargs
2. for do not know how many variable <-> for do not know what kinds of information
3. accept as a tuple <-> accept as key-value pairs
   
# repeater
```python
def repeater(*stuff, **more_stuff):
    for name in stuff:
        print(name)
    for key, value in more_stuff
        print(key, value)

repeater('name_a','name_b',name='name_c')
```

# documenting
1. use triple quotation mark under the function head.
2. Short one sentence to describe the purpose of this function
3. one blank line
4. addition comments if one sentence is not enough
5. param: describe what the user should pass argument to this function
6. precondition: the user should meet the precondition before using this function
7. postcondition: if precondition is met, postcondition will show what the function will do
8. return: describe what this function will return if precondition is met.

# tuple vs. set
1. parentheses <-> curly braces
2. immutable <-> mutable
3. order <-> no order

# comparing floats
We cannot compare two floats by float_A == float_B because representation error, for example 1/3. Instead, we use tolerance to check whether two float number are close or not.
```python
tolerance = 0.0001
if abs(float_A - float_B) < tolerance:
    print('These two float number are close')
```
We also can use math.isclose(float_A, float_B) to check it.

# view <-> iterator
1. view
    View is a dynamic and virtual sequence. We can iterate a view. These 3 dictionary methods can return a view: items(), keys(), values()
```python
for key in dictionary_1.keys():
    print(key)
```

2. iterator
    If we pass an iterable to iter(), it will create a iterator object. Then, we can use next() to iterate this object until it raise StopIteration exception
```python
list_1 = [1,2,3]
list_1_object = iter(list_1)
next(list_1_object)
next(list_1_object)
next(list_1_object)
```

# privacy and encapsulation when developing class:
we use dunder to create a private variable in the class
```python

class Dod()
    def __init__(self, name):
        self.__name = name
``` 