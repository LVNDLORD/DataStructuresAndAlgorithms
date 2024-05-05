"""
Implement a Dijkstra's shortest path function
Given the information you have received about Dijkstra's shortest path algorithm, implement a function that finds
the shortest path from a source vertex to a destination vertex. The function accepts as parameters the source vertex,
the destination vertex and the graph to work with. The function returns a tuple containing
the minimum distance between vertices and a list of vertices that form the minimum path from one vertex to the other.

As a reminder, the graph object offers some methods that can be used in this case:

get_vertices(): Return a list of vertices on the graph
get_vertices(u): Return a list of the adjacent vertices of a given vertex
get_edges(): Return a set of all edges of the graph.
get_edge(u, v): Returns the edge from u to v, or None if not adjacents.
degree(u): Returns the number of edges incident to vertex u.
get_adjacent_vertices(u): Return a list of the adjacent vertices of a given vertex
get_incident_edges(u): Returns edges incident to vertex u.
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

    def get_weight(self):
        return self.weight


class Graph:
    def __init__(self, adj_map):
        self.adj_map = adj_map

    def get_vertices(self):
        """
        Get all vertices in the graph.
        """
        return list(self.adj_map.keys())

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
        if start in self.adj_map and end in self.adj_map[start]:
            return self.adj_map[start][end]
        else:
            return None


def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    """
    Calculate the shortest past (in distance value) between given vertices using Dijkstra's algorithm.

    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question

    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[source_vertex] = 0
    predecessors = {vertex: None for vertex in graph.get_vertices()}
    visited = set()

    while len(visited) < len(graph.get_vertices()):
        min_vertex = None
        min_distance = float('inf')
        for vertex in graph.get_vertices():
            if vertex not in visited and distances[vertex] < min_distance:
                min_vertex = vertex
                min_distance = distances[vertex]

        if min_vertex is None:
            break

        visited.add(min_vertex)

        for neighbor_vertex in graph.get_adjacent_vertices(min_vertex):
            edge = graph.get_edge(min_vertex, neighbor_vertex)
            if edge is None:
                continue
            distance_through_current = distances[min_vertex] + edge.get_weight()
            if distance_through_current < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance_through_current
                predecessors[neighbor_vertex] = min_vertex

    path = []
    current_vertex = destination_vertex
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = predecessors[current_vertex]

    return distances[destination_vertex], path


# Define vertices and edges
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

# Construct adjacency map
adj_map = {
    A: {B: AB, C: AC},
    B: {A: AB, D: BD},
    C: {A: AC, D: CD, E: CE},
    D: {B: BD, C: CD, F: DF},
    E: {C: CE, F: EF},
    F: {D: DF, E: EF}
}

# Print adjacency map
print("Adjacency Map:")
for vertex, edges in adj_map.items():
    print(vertex, ": ", end="")
    for adjacent_vertex, edge in edges.items():
        print(adjacent_vertex, f"({edge.get_weight()})", end=", ")
    print()

# Construct graph
g = Graph(adj_map)

# Run Dijkstra's algorithm
print(dijkstra_shortest_path(A, F, g))
