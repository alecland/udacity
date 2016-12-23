import math

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1;
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1;
    return G

# Make an empty graph
a_grid = {}

# Number of nodes per side is the square root of the total number of nodes
n = 256
side = int(math.sqrt(n))

# Add in the edges
# Each node is identified by its two coordinates (i,j)
# For each node, if it's not in the very edge, make a link downward and a link to the right
for i in range(side):
    for j in range(side):
        if i < side - 1: make_link(a_grid, (i,j), (i+1,j))
        if j < side - 1: make_link(a_grid, (i,j), (i,j+1))

# How many nodes ?
print(len(a_grid))

# How many edges ?
print(sum([len(a_grid[node]) for node in a_grid.keys()])/2)
