from collections import deque

#  Suppose that we have a mango tree and we want to sell mangoes
# To sell mangoes we need a seller. We decided to look for a seller in our Facebook profile.

# Firstly we want check from the friend list, if we have a friend who is selling mangoes
# We add our "direct" friends to the seller_list and check for each of the friend.
# If a friend is not a mango seller we add all his friends to the seller_list.
# We keep doing this until we find a mango seller or we run out of friends.
# For this example, a mango seller is a person with 'm' last letter in the name

# To store relationship between friends we use lists inside of the dictionaries
# RECALL graphs in algorithm. What are the edges and what are the vertices? What are the directed and undirected graphs?

graph = dict()
graph["ali"] = ["alice", "bob", "claire"]  # In this example I have 3 friends on Facebook: alice, bob and claire.
graph["bob"] = ["anuj", "peggy"]  # anuj and peggy are friends of bob and are "not" my friends
graph["alice"] = ["peggy"]  # alice has also peggy in her friends list
graph["claire"] = ["thom", "jonny"]  # claire has two in the friend list that I don't have
graph["anuj"] = []  # all anuj friends friends are also my direct friends
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# Closer friends are in the priority to the position. To accomplish this we use queues. Queues are similar to the real
# life queue. They called a FIFO data structure: First In, First Out.
# In contrast, a stack is a LIFO data structure: Last In, First Out.

def search(name):  # start from person myself
    search_queue = deque()  # creates a new queue
    search_queue += graph[name]  # gives a list of friends from the dictionary
    searched = []  # to not go through the same name again, store searched names in a list
    while search_queue:  # until there are elements in the queue
        person = search_queue.popleft()  # we remove the first element (leftmost)
        if person not in searched:  # if the name appears for the first time
            if person_is_seller(person):  # invokes function that checks if a person a seller or not
                print(person + " is a mango seller!")  # give a name of the seller
                return True  # ends the function
            else:  # if the person is not a mango seller
                search_queue += graph[person]  # add all his friends to the list
                searched.append(person)  # add his name to the searched list
    return False  # if no one in the queue was a mango seller the function will return False


def person_is_seller(name):
    return name[-1] == "m"  # returns True if last letter of the name is 'm'


search("ali")  # prints tom is a mango seller!


# In the worst scenario we would have to search for every one, that means we'll follow each edge. So the running time is
# at leas O(number of edges). We also keep a queue of every person to search. Adding one person to the queue takes
# constant time: O(1). Doing this for every person will take O(number of people) total. In total, breadth-first search
# takes O(number of people + number of edges) and it's more commonly written as O(V+E) (V for number of vertices, E for
# number of edges).
