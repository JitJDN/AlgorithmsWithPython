# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

ef find_eulerian_tour(graph):
    
    tree = {}
    for i in graph:
        v1, v2 = i
        if v1 in tree:
            tree[v1].append(v2)
        else:
            tree[v1] = [v2]

        if v2 in tree:
            tree[v2].append(v1)
        else:
            tree[v2] = [v1]

    return tree

inputgraph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(inputgraph)