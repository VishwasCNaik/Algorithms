class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Add a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at a specific index
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Delete the first occurrence of data
    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    # Search for a value in the list
    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    #Return a list of all elements
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"
