# In Dijkstras algorithm, you assign number or weights to each segment. 
# Then Dijkstra's algorithm finds the path with the smallest total weights
# There are 4 steps:
# 1. Find the cheapest node. This is the node you can get to in the least amount of time
# 2. Check whether there is a cheaper path to the neighbours of this node, If so update their costs
# 3. Repeat until youve done this for every node in the graph
# 4. Calculate the final path  
# ---------------------------------------------------------------------------------------
# Trading for a piano example - Rama is trying to trade a music book for a piano
# In the graph the nodes are all the items Rama can trade for
# The weights and edges are the amount of money he would have to pay to make the trade
# How is Rama going to figure out the path from the book to the piano where he spends the least amount of dough?


# the graph
graph ={}
# this hashtable has more hashtables inside
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table
# the cost of a node is how long it takes toto that node from start
# you dont know how long it takes to get to finish
# if you dont know the cost yet, you put down infinity
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# you need an array to keep track of the nodes you've already processed
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasnt been processed yet...
        if cost < lowest_cost and node not in processed:
            #...set it as the new lowest-cost node 
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet 
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node
    neighbors = graph[node]
    # loop through the neighbors
    for n in neighbors.keys():
        # calculating how long it would take to get to node A if you went Start > node B > node A
        #instead of Start > node A
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor
            parents[n] = node
    # Mark the node as processed
    processed.append(node)
    # Find the next node to process, and loop
    node = find_lowest_cost_node(costs)

print("Cost from the start of each node:")
print(costs)





