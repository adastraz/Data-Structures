class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
            self.size += 1

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.size -= 1
            return value