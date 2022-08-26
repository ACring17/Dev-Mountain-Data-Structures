class Node(object):
  """Node in a linked list."""

  def __init__(self, data):
      self.data = data
      self.next = None

  def __repr__(self):
      return f"<Node object. Data: {self.data}; Next: {self.next.data if self.next else None}>"


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked List. Head: {self.head.data if self.head else None}; Tail: {self.tail.data if self.head else None}>"

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def remove(self, value):
        """Remove node with given value"""

        # If removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Removing something other than head
        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    # If removing last item, update .tail
                    self.tail = current
                return

            else:     # haven't found yet, keep traversing
                current = current.next
    
    def get_length(self):
        """
        This method returns the length of a linked list.
        """
        length = 1

        current = self.head

        while current != self.tail:
            length += 1
            current = current.next

        return length


def shorten_word(words):
    new_list = words[1:]

    new_ll = LinkedList()

    for i in new_list:
        new_ll.append(i)

    return new_ll


test_list = ["Red", "Blue", "Green", "Orange", "Pink", "Brown"]

my_ll = shorten_word(test_list)

print(my_ll.get_length())