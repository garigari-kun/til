# Describing a graph dict
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# Describing a cost dict
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Describing a parents dict
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_in_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_in_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor, neighbor_cost in neighbors.items():
        new_cost = cost + neighbor_cost
        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_in_lowest_cost_node(costs)




















# end
