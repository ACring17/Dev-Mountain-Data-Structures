class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

    def total_nodes(self):
        """A method that returns all the nodes in this trees. It only needs to take it self as the parameter, and because self is implied when called, zero arguments when invoked."""

        def num_children(node, current_total):
            inner_nodes = current_total

            for child in node.children:
                inner_nodes += 1
                inner_nodes = num_children(child, inner_nodes)

            return inner_nodes
            
        return num_children(self.root, 0)


def make_tree(ceo, direct_reports_list):
    """Takes in a CEO as a string, and a list of strings representing the CEO's direct reports."""

    node = Node(ceo, direct_reports_list)
    return Tree(node)

if __name__ == '__main__':

    resume = Node("resume.txt", [])
    recipes = Node("recipes.txt", [])
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py", [])
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/root", [users])

    tree = Tree(root)
    print("server.py = ", tree.find_in_tree("server.py"))
    print("style.css = ", tree.find_in_tree("style.css"))

    print(f"Total nodes are {tree.total_nodes()}")