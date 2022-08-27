class Node():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<Node: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

    def print_friends(self):
        """Function that prints the name of all our friends."""

        for friend in self.nodes:
            print(friend.name)


andrew = Node("Andrew")
ben = Node("Ben")
nick = Node("Nick")
matt = Node("Matt")
casey = Node("Casey")
anna = Node("Anna")
gabby = Node("Gabby")
jackson = Node("Jackson")
trevor = Node("Trevor")

friends = FriendGraph()
friends.add_people([andrew, ben, nick, matt, casey, anna, gabby, jackson,trevor])

friends.set_friends(andrew, ben)
friends.set_friends(andrew, trevor)
friends.set_friends(ben, trevor)
friends.set_friends(nick, casey)
friends.set_friends(nick, jackson)
friends.set_friends(casey, anna)
friends.set_friends(anna, matt)
friends.set_friends(gabby, jackson)
friends.set_friends(jackson, matt)

friends.print_friends()