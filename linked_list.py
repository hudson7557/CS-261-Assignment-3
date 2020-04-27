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

        # if the index is less than 0 raise range exception
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
            index: The index of the node that will be removed
        """

        # if the index is less than 0 raise range exception
        if index < 0:
            raise Exception('Index out of range')

        cur = self.head
        prev = None

        if index == 0:
            self.head.next = cur.next

        # go through the linked list until we find the specified index
        for number in range(index + 1):
            # if cur ever becomes the tail sentinel we raise a range exception
            if cur == self.tail:
                raise Exception('Index out of range')
            prev = cur
            cur = cur.next

        # I don't delete my own Nodes, I have people for that, or... python.
        prev.next = cur.next

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        new_link.next = self.head.next  # set new_link next to the next Node
        self.head.next = new_link  # set the front sentinel to point to new_link

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

        if self.head.next == self.tail:
            return None

        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is
            no such node
        """

        if self.head.next == self.tail:
            return None

        cur = self.head
        prev = None

        while cur != self.tail:
            prev = cur
            cur = cur.next

        return prev.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # if the list is empty nothing happens.
        if self.head.next == self.tail:
            return

        # change the next data members to point to skip the first Node
        cur = self.head.next
        self.head.next = cur.next

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        cur = self.head
        prev = None

        # since it's single link we need to go through the list to find the last
        # Node which points to the end of the list. We then set the previous to
        # skip the last Node.
        while cur.next != self.tail:
            prev = cur
            cur = cur.next

        prev.next = self.tail

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.head.next == self.tail:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        cur = self.head

        # sort through the list checking the data of each Node, if found return
        # True.
        while cur != self.tail:
            if cur.data == value:
                return True
            cur = cur.next

        # if the value is not found we return False.
        else:
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        cur = self.head
        prev = None

        while cur != self.tail:

            # check each Node to see if it contains our target value
            if cur.data == value:
                # if the value is found we change prev.next to point to skip the
                # current Node.
                prev.next = cur.next
                return

            prev = cur
            cur = cur.next

        return


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

        # if the list is empty we set both next and prev on the sentinel
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link

        # if the list isn't empty we just set next on the sentinel
        else:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link

        return

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty we set both next and prev on the sentinel
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link

        # if the list isn't empty we just set next on the sentinel
        else:
            new_link.prev = self.sentinel.prev
            new_link.next = self.sentinel
            self.sentinel.prev.next = new_link
            self.sentinel.prev = new_link

        return

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        return self.sentinel.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        return self.sentinel.prev.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        if self.sentinel.next == self.sentinel:
            return False
        else:
            self.sentinel.next.next.prev = self.sentinel
            self.sentinel.next = self.sentinel.next.next

            return True

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        if self.sentinel.prev == self.sentinel:
            return False
        else:
            self.sentinel.prev.prev.next = self.sentinel
            self.sentinel.prev = self.sentinel.prev.prev

            return True

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        if self.sentinel.next == self.sentinel:
            return False
        else:
            cur = self.sentinel.next
            while cur != self.sentinel:
                if cur.data == value:
                    return True
                cur = cur.next

            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        cur = self.sentinel.next
        while cur != self.sentinel:
            if cur.data == value:
                if cur.prev != self.sentinel and cur.next != self.sentinel:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next

                # handles a value at the front of the list
                if cur.prev == self.sentinel and cur.next != self.sentinel:
                    self.sentinel.next = cur.next
                    cur.next.prev = self.sentinel

                # handles a value at the end of the list
                if cur.prev != self.sentinel and cur.next == self.sentinel:
                    self.sentinel.prev = cur.prev
                    cur.prev.next = self.sentinel

                return True

            cur = cur.next
        return False

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new
        links to do so. (e.g. you cannot call DLNode()). If the list printed by
        following next was 0, 1, 2, 3, after the call it will be 3,2,1,0
        """

        # FIXME: Write this function

# fucking update