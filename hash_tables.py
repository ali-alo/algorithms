# A hash function is a function where you put in a string and you get back a number.
# Has tables are very fast. They have the following Big O notation O(1) for search, insert and delete.
# Two distinct elements (keys in our example) assigned to the same slot is a collision.
# Good hash function has minimum amount of collisions.
# Once the load factor is greater than 0.7, it's time to resize the hash table.

# Python language has built-in hash tables: dictionary. And the output of the key can be any data type, not numbers only
# To initialize a dictionary:

fruits = dict()
print(type(fruits))  # prints class dict

# or
book = {}
print(type(book))  # prints class dict

# to add key and its value to the dict
book["apple"] = 0.67  # apples for 67 cents
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)  # prints {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}

# we can quickly and easily access price of product by just entering their names (keys)
print(book["avocado"])  # prints 1.49

# hash tables are great for catching duplicates

# Imagine a fair election. If someone has already voted we can quickly find that, no matter how long our dictionary is

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Sorry you already voted")
    else:
        voted[name] = True
        print("Please vote!")


check_voter("Alice")  # prints Please vote!
check_voter("Bob")  # prints Please vote!
check_voter("Alice")  # prints Sorry you already voted
