"""
Implement a BFS traversal function for a graph
With the information you have received from the course, implement a Breadth-First traversal iterative function
for a graph. The function accepts as parameters the graph object and the vertex from where to start.

The function should return a dictionary with the vertices as the keys and the vertices from where those keys where
visited as the values.
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

    def get_adjacent_vertices(self, vertex):
        """
        Get adjacent vertices of a given vertex.
        """
        if vertex in self.adj_map:
            return list(self.adj_map[vertex].keys())
        else:
            return []

    def get_edge(self, start, end):
        """
        Get the edge between two vertices.
        """
        return self.adj_map[start][end]


def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    discovered = {start: None}
    level = [start]
    while level:
        next_level = []
        for u in level:
            for v in graph.get_adjacent_vertices(u):
                if v not in discovered:
                    discovered[v] = u
                    next_level.append(v)
        level = next_level
    return discovered


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

adj_map1 = {
    A: {B: AB, C: AC},
    B: {A: AB, D: BD},
    C: {A: AC, D: CD, E: CE},
    D: {B: BD, C: CD, F: DF},
    E: {C: CE, F: EF},
    F: {D: DF, E: EF}
}

g = Graph(adj_map1)
print(BFS(g, A)) # {<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: C>: <Vertex: A>, <Vertex: D>: <Vertex: B>,
# <Vertex: E>: <Vertex: C>, <Vertex: F>: <Vertex: D>}

