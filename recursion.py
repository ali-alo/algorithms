# Function called by itself is a recursion.

# Imagine that you have a large box with medium boxes inside which have smaller boxes inside and so on
# In one of the boxes (can be large, can be small) there is a key. To find the key we can use recursion

def find_key(box):
    for item in box:
        if item.is_a_box():
            find_key(item)  # recursion
        elif item.is_a_key():
            print("found a key!")


# Common problem with recursion is infinite looping.
# The sample countdown infinite recursion function is shown below

# def countdown(i):
#     print(i)
#     countdown(i * 1.2)
#
#
# countdown(2)

# End result: RecursionError: maximum recursion depth exceeded while calling a Python object


# Every correct recursion has two parts: the base case, and the recursive case.
# The recursive case is when the function calls itself
# The base case is when the function stops calling itself and leave the recursion, so it doesn't go into infinite loop

# Now let's rewrite the incorrect countdown function above

def correct_countdown(i):
    print(i)
    if i <= 0:  # base case
        return
    else:  # recursive case
        correct_countdown(i - 1)


correct_countdown(3)
""" 
prints
    3
    2
    1
    0
"""

# Call stack tells what function is currently being run and what functions have been run and not finished yet
# A stack has two operations: push and pop. (recall example with barbeque)
# The call stack can gets very long, which takes up a lot of memory

# The simplest example


# function greet is executed in which another two functions are going to be executed
def greet(name):
    print("hello " + name + "!")
    greet2(name)  # greet2 function is now on top of the call stack, however greet function is not finished yet
    print("getting ready to say bye...")
    bye()  # bye function is now on top of the call stack, greet function under it
    # only now greet function pops out from the call stack


def greet2(name):
    print("how are you, " + name + "?")
    # after the execution of the line above, greet2 function pops out of the call stack


def bye():
    print("ok bye!")
    # after the execution of the line above, bye function pops out of the call stack


greet("maggie")


# Example of call stack with recursion

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)  # 2 * 3 * 4 * 5


print(fact(5))  # prints 120
