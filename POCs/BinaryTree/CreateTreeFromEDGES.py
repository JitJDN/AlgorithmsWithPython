# Create Tree From EDGES
def createTreeFromEdges(edges):
    tree = {}
    for i in edges:
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

edges = [[2, 1], [3, 2], [4, 2], [5, 1], [6, 1], [7, 1], [8, 7]]
print createTreeFromEdges(edges)

def createTreeFromEdges(edges):
    tree = {}
    for v1, v2 in edges:
        tree.setdefault(v1, []).append(v2)
        tree.setdefault(v2, []).append(v1)
    return tree

def setdefault(self, key, default=None):
    if key not in self:
        self[key] = default
    return self[key]

edges = [[2, 1], [3, 2], [4, 2], [5, 1], [6, 1], [7, 1], [8, 7]]
print createTreeFromEdges(edges)