# graphs model a set of connections - graphs are made up of nodes and edges
# breadth first search runs on graphs and can help answer two types of questions:
# 1. Is there a path from node A to node B?
# 2. what is the shortest path from node A to node B?
# -----------------------------------------------------

# Suppose you're looking for a mango seller who can sell your mangoes
# Are you connected to a mango seller on Facebook? - Search through your friends
# 1. make a list of friends to search
# 2. Now go through each person in the list & check whether tht person selles mangoes
# 3. Suppose none are mango sellers. Now you have to search through your friend's friends

# with this algorithm you'll search your entire network until you come across a mango seller

from collections import deque

# This function tells you when someone is a mango seller 
def person_is_seller(name):
# checks whether a persons name ends with the letter m. 
# If it does than theyre a mango seller - kind f a silly way to do it
    return name[-1] == 'm'

graph = {}
# notice "you" is mapped to an array
# so graph["you"] will give you an array of all the neighbors of "you"
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    #creates a new queue
    search_queue = deque()
    # adds all your neighbours to the search queue
    search_queue += graph[name]
    # this array is how you keep track of which people you've searched before
    searched = []
    #while the queue isnt empty
    while search_queue:
        # ...grabs the first person off the queue
        person = search_queue.popleft()
        # only search this person if you havent already searched them
        # checks whether the person is a mango seller
        if person not in searched:
            if person_is_seller(person):
                #yes theyre a mango seller
                print(person + " is a mango seller!")
                return True
            else:
                # no they arent. Add all of this persons friends to the search queue
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    # If you reached here, no one in the queue was a mango seller
    return False

search("you")

# If there is a path breadth first search will find the shortest path
# If you have a problem like "find the shortest X" try modeling your problems as a graph and  use breadth first search to solve
# Queues are FIFO (first in first out)
# Stacks are LIFO (last in first out)