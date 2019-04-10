import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or\
                userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        # Loop to generate users
        for i in range(0, numUsers):
            self.addUser(f"User{i}")
        # Create friendships
        possibleFriendships = []  # Friendship list
        for userID in self.users:  # Loop through users
            for friendID in range(userID + 1, self.lastID + 1):
                # Loops through all possible friends
                # Adds friends to list
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)  # Shuffles possible friendships
        for i in range(numUsers * avgFriendships // 2):
            # Loops through friendships and creates friendships
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([userID])
        while q.size > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for friend in self.friendships[v]:
                    if friend not in visited:
                        path_copy = list(path)
                        path_copy.append(friend)
                        q.enqueue(path_copy)
        # lengths = []
        # for key in visited.items():
        #     lengths.append(len(visited[key]))
        # return sum(lengths)/len(lengths)
        return visited


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


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 5)
    print(f"FriendShips: \n\n {sg.friendships}")
    connections = sg.getAllSocialPaths(1)
    print("\n")
    print(f"Connections: \n\n {connections}")
