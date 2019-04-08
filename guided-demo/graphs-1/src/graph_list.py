"""Graph representation using adjacency list."""


class Edge:
    """Edges in the adjacency list are just a destination."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods

    def __init__(self, destination):
        self.destination = destination


class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods

    def __init__(self, label):
        self.label = label
        self.edges = set()


class Graph:
    """The graph itself is simply a set of vertices."""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        self.vertices = set()

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
# Stack helper class


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.size = 0
    # what data structure should we
    # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size
