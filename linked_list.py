# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


"""
*******************************************************************************
Part1: Deque and Bag implemented with Linked List
*******************************************************************************
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

        # if the list is empty the node is placed at the beginning
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

        # moving through the list
        for number in range(index + 1):

            # if the current Node ever becomes the tail sentinel we raise
            # an index exception.
            if cur == self.tail:
                raise Exception('Index out of bounds')

            prev = cur
            cur = cur.next

        # the for loop has targeted the correct index, we can now insert the
        # node into the list.
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

        # if the list is empty return None
        if self.head.next == self.tail:
            return None

        # otherwise we return the data of the first Node.
        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is
            no such node
        """

        # if the list is empty returns None.
        if self.head.next == self.tail:
            return None

        cur = self.head
        prev = None

        # flips through the list until the tail is reached and then returns the
        # previous node
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
            return False

        # change the next data members to point to skip the first Node
        cur = self.head.next
        self.head.next = cur.next
        return True

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
        return

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # returns true if the list is empty
        if self.head.next == self.tail:
            return True

        # otherwise returns false
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

        # if the value is not found return False.
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
*******************************************************************************
Part 2: 9898-465-7436 is the zoom meeting id 
*******************************************************************************
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

        # handle an index out of range
        if index < 0:
            raise Exception('Index out of range')

        # if the index is zero the new node is inserted at the beginning.
        if index == 0:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link
            return True

        # if the index is anything else
        cur = self.sentinel.next
        for num in range(index):
            cur = cur.next
            if cur == self.sentinel:
                # if the index is out of range we raise an exception
                raise Exception('Index out of range')

        new_link.prev = cur.prev
        cur.prev.next = new_link
        new_link.next = cur
        cur.prev = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            index: The index of the node that will be removed
        """
        if self.sentinel.next == self.sentinel:
            return False

        # handle an index out of range
        if index < 0:
            raise Exception('Index out of range')

        cur = self.sentinel.next
        for num in range(index):
            cur = cur.next
            if cur == self.sentinel:
                raise Exception('Index out of range')

        # if the Node we are removing is not linked to the sentinel
        if cur.prev != self.sentinel and cur.next != self.sentinel:
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

        # if the Node we are removing is in the front of the DL list
        if cur.prev == self.sentinel and cur.next != self.sentinel:
            cur.next.prev = self.sentinel
            self.sentinel.next = cur.next

        # if the Node we are removing is in the back of the DL list
        if cur.prev != self.sentinel and cur.next == self.sentinel:
            cur.prev.next = self.sentinel
            self.sentinel.prev = cur.prev

        # if the list contains only one Node in it
        if cur.prev == self.sentinel and cur.next == self.sentinel:
            self.sentinel.prev = self.sentinel
            self.sentinel.next = self.sentinel

        return True

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
            The data in the node at last index of the list or None if there is
            no such node
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

                # handles a non-end value
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

        # set a base case where we are looking at the 1st and 2nd node
        cur = self.sentinel.next
        next_node = cur.next

        # takes a Node and flips their prev and next values
        while cur != self.sentinel:
            cur.next = cur.prev
            cur.prev = next_node
            cur = next_node
            next_node = cur.next

        # since hitting the sentinel is what stops the loop we have to
        # manually set the prev and next values for sentinel to close the loop
        hold_me = cur.prev
        cur.prev = cur.next
        cur.next = hold_me
        return
