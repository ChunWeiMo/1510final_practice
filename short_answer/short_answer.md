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