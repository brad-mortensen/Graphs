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
