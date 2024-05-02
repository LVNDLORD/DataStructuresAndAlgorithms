"""
Implement a DFS traversal function for a graph
With the information you have received from the course, implement a Depth-First traversal recursive function for a graph.
The function accepts as parameters the graph object, the vertex from where to start and a visited dictionary
(that defaults to None, so the final user don't need to provide it)

The function should return a dictionary with the vertices as the keys and the vertices from where those keys
where visited as the values.
"""


class Vertex:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"<Vertex: {self.label}>"


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self, adj_map):
        self.adj_map = adj_map


def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """
    if visited is None:
        visited = {}

    visited[u] = None  # Mark current vertex as visited

    for neighbor in graph.adj_map[u]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
            visited[neighbor] = u

    return visited


A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

AB = Edge(A, B, 2)
AC = Edge(A, C, 4)
BD = Edge(B, D, 5)
CD = Edge(C, D, 9)
CE = Edge(C, E, 3)
DF = Edge(D, F, 2)
EF = Edge(E, F, 2)

adj_map = {
    A: {B: AB, C: AC},
    B: {A: AB, D: BD},
    C: {A: AC, D: CD, E: CE},
    D: {B: BD, C: CD, F: DF},
    E: {C: CE, F: EF},
    F: {D: DF, E: EF}
}

g = Graph(adj_map)
print(DFS(g, A)) # {<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: D>: <Vertex: B>, <Vertex: C>: <Vertex: D>,
# <Vertex: E>: <Vertex: C>, <Vertex: F>: <Vertex: E>}

