from queue_stack import *
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2]. add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1] = v2
        else:
            raise IndexError("That vertex doesnt exist")

    def bfs(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            print(v)
            visited.add(v)
            for next_vert in self.vertices:
                q.enqueue(next_vert)

    def dfs(self, starting_vertex_id):
        stack = Stack()
        stack.push(starting_vertex_id)
        visited = set()
        while stack.size() > 0:
            v = s.pop()
            print(v)
            visited.add(v)
            for next_vert in self.vertices[v]:
                s.push(next_vert)


seasons = Graph()
seasons.add_vertex("Spring")
seasons.add_vertex("Summer")
seasons.add_vertex("Fall")
seasons.add_vertex("Winter")
seasons.add_directed_edge("Spring", "Summer")
seasons.add_directed_edge("Summer", "Fall")
seasons.add_directed_edge("Fall", "Winter")
seasons.add_directed_edge("Winter", "Spring")
print(f"Seasons Graph: {seasons.vertices}")
test_graph = Graph()
test_graph.add_vertex(1)
test_graph.add_vertex(2)
test_graph.add_vertex(3)
test_graph.add_vertex(4)
test_graph.add_vertex(5)
test_graph.add_vertex(6)
test_graph.add_vertex(7)
test_graph.add_edge(1, 2)
test_graph.add_edge(1, 3)
test_graph.add_edge(2, 4)
test_graph.add_edge(2, 5)
test_graph.add_edge(3, 6)
test_graph.add_edge(3, 7)
print(f"Test Graph: {test_graph.vertices}")
