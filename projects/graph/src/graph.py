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
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1] = v2
        else:
            raise IndexError("That vertex doesnt exist")

    def bfs(self, starting_vertex_id, target_vortex):
        # Create an empty queue
        q = Queue()
        # Create a visited set
        path = []
        path.append(starting_vertex_id)
        visited = set()
        # Enqueue [A PATH TO] the starting vertex to the queue
        q.enqueue(path)
        # While the queue is not empty...
        while q.size > 0:
            v = q.dequeue()
            if v[-1] not in visted:
                visited.add(v[-1])
                if v[-1] == target_vortex:
                    return path
                for next_vert in self.vertices[v[-1]]:
                    path.append(next_vert)
                q.enqueue()    
            # Dequeue the first [PATH] from the queue
            # PULL THE LAST VERTEX FROM THE PATH
            # Check if it's visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S EQUAL TO THE TARGET VERTEX
                # IF IT IS, RETURN THE PATH
                # Put [A PATH TO] all of its neighbors in the back of the queue
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR VERTEX TO THE PATH
                    # ENQUEUE THE NEW PATH

    def dfs(self, starting_vertex_id, search_query):
        pass

# Implement the queue, and enque the starting Vertex ID
    def bft(self, starting_vertex_id):
        # Create and empty queue
        q = Queue()
        q.enqueue(starting_vertex_id)
        # Create a set to store vertices
        visited = set()
        # While the queue is not empty"
        while q.size > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            if v not in visited:
                # If that vertex has not been visited:
                # Mark it as visited
                print(v)
                visited.add(v)
        # Add all of its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        s.push(starting_vertex_id)
        # Create a set to store vertices
        visited = set()
        # While the stack is not empty"
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited:
            # Mark it as visited
            if v not in visited:
                print(v)
                visited.add(v)
            # Add all of its neighbors to the top of the stack
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
# seasons.dft("Summer")
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
test_graph.bft(1)
print(f"Test Graph: {test_graph.vertices}")
