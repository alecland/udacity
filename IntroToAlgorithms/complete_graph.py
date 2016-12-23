def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1;
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1;
    return G

# How many edges on a complete graph of n nodes ?
# Add in the edges

def clique(n):
    a_complete = {}
    for i in range(n):
        for j in range(n):
            if i<j: make_link(a_complete, i, j)
    return (sum([len(a_complete[node]) for node in a_complete.keys()])/2)

for n in range(1,10):
    print(clique(n));

