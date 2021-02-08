# Breadth-first algorithm works great with graph, however, we cannot use it when weighted graphs.
# When we are working with weighted graphs (when each edge has a certain cost), we use Dijkstra's algorithm

# Sometimes with weighted graphs a detour (passing through more vertexes) can lead to a lower cost of reaching a
# vertex. However, Dijkstra's algorithm is not appropriate with negative weigh of edges. In this situation we use
# Bellman-Ford algorithm.

# Dijkstra's algorithm works also only with directed acyclic graph DAG. That is, all edges must be directed (there
# should be edges that point to each other) and there should not be "trap edge" where we can fall in an infinite loop.

# To use Dijkstra's algorithm we have to create 3 hash tables: graph (where we will store edges to other nodes),
# costs (where we will store and update costs from one node to another) and parents (to update our rote).

# Implementation

# store connection between edges in the graph hash table
graph = dict()
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# for additional information
# print(graph["start"].keys())
# print(graph["start"]["a"])
# print(graph["start"]["b"])

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# because we do not know the total coast to reach the end point we set the cost infinity
infinity = float("inf")

# as for now we only now the cost from the start point to the two first nodes.
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents hash table is needed to update and later on trace the route.
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# nodes should not be calculated again, as we identify the lowest coast to the node we append him to the list below
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # go through each node
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # if it is the lowest cost one and hasn't been processed yet..
            lowest_cost = cost  # set it as a new lowest-cost node
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # find the node with the lowest-cost node, that we haven't processed yet
while node is not None:  # if we have processed all the nodes, this while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # go through all the neighbours of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # If it is cheaper to get to this neighbour by going through this node
            costs[n] = new_cost  # update the cost for the node, as it is cheaper now
            parents[n] = node  # this node becomes a new parent of the just updated node
    processed.append(node)  # add the processed node to the list, so we won't go through it again
    node = find_lowest_cost_node(costs)  # find the next node to process, and loop

print(costs["fin"])  # 6




