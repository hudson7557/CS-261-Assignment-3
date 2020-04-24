# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


"""
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
"""


class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly
            added node
        """
        if index < 0:
            raise Exception('Index out of range')

        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty the node is just placed at the beginning
        if self.head.next == self.tail:
            new_link.next = self.tail
            self.head.next = new_link
            return

        # if the index is 0 the new Node is placed at the start of the list.
        if index == 0:
            new_link.next = self.head.next
            self.head.next = new_link
            return

        # inserts the node at the specified index
        cur = self.head
        prev = None

        for number in range(index + 1):
            # if the current Node ever becomes the tail sentinel we raise
            # an index exception.
            if cur == self.tail:
                raise Exception('Index out of bounds')
            prev = cur
            cur = cur.next

        # inserts the node in the list.
        new_link.next = cur
        prev.next = new_link
        return

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        new_link.next = self.head.next # set new_link next to the next Node
        self.head.next = new_link # set the front sentinel to point to new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        cur = self.head
        prev = None

        # since it's single link we need to go through the list to find the end
        # not the most efficient. O(n)?
        while cur != self.tail:
            prev = cur
            cur = cur.next

        # once we've found the end of the list we insert our new_link
        new_link.next = cur
        prev.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXME: Write this function

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXME: Write this function

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXME: Write this function


'''
**********************************************************************************
Part 2: 9898-465-7436 is the zoom meeting id 
**********************************************************************************
'''


class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None
        data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly
            added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXME: Write this function

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXME: Write this function

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new
        links to do so. (e.g. you cannot call DLNode()). If the list printed by
        following next was 0, 1, 2, 3, after the call it will be 3,2,1,0
        """

        # FIXME: Write this function

ml = LinkedList()




ml.add_back('A')
ml.add_front('Z')
print(ml.__str__())
ml.add_link_before('A', 0)
ml.add_link_before('B', 0)
print(ml.__str__())
ml.add_link_before('C', 1)
print(ml.__str__())
ml.add_link_before(80, 1)
print(ml.__str__())
ml.add_link_before(40, 2)
print(ml.__str__())
# ml.add_link_before(44, -1)
# ml.add_link_before(44, 20)
ml.add_front('A')
ml.add_back('A')
print(ml.__str__())
