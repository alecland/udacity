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

def find_eulerian_tour(graph):
    # your code here
    res = []
    res.append(graph[0][0])
    res.append(graph[0][1])
    del graph[0]
    length = len(graph)
    while (length > 0):
        for i in range(length):
            # print res[-1];
            if graph[i][0] == res[-1]:
                res.append(graph[i][1])
                del graph[i]
                break
            if graph[i][1] == res[-1]:
                res.append(graph[i][0])
                del graph[i]
                break
        if length == len(graph):
            res = []
            break
        else:
            length = len(graph)
            
    return res


input1 = [(1, 2), (2, 3), (3, 1)]
input2 = [(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
input3 = [(1, 13), (1, 6), (6, 11), (3, 13),(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),(1, 12), (4, 12), (5, 14), (0, 1),(2, 3), (4, 11),(6, 9),(7, 14),(10, 13)]
input4 = [(8, 16), (8, 18), (16, 17), (18, 19),(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
print (find_eulerian_tour(input1))
print (find_eulerian_tour(input2))
print (find_eulerian_tour(input3))
print (find_eulerian_tour(input4))
