import gc


class Node:
    def __init__(self, key, value):
        self.next = None
        self.previous = None
        self.value = value
        self.key = key


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, key, value):
        node = Node(key, value)
        node.next = self.head

        if self.head:
            self.head = node
            self.head.previous = node
            return node
        else:
            self.head = self.tail = node
            return node

    def push_back(self, key, value):
        node = Node(key, value)
        node.previous = self.tail

        if not self.tail:
            self.head = node
            self.tail = node
            return node
        else:
            self.tail.next = node
            self.tail = node
            return node

    def pop_front(self):
        if not self.head:
            return
        else:
            node = self.head
            node.next.previous = None
            self.head = node.next
            node.next = None
            gc.collect()
            return node

    def pop_back(self):
        if not self.tail:
            return
        else:
            node = self.tail
            node.previous.next = None
            self.tail = node.previous
            node.previous = None
            gc.collect()
            return node

    def pop_node(self, node):
        if not node.previous:
            self.head = node.next
        else:
            node.previous.next = node.next

        if not node.next:
            self.tail = node.previous
        else:
            node.next.previous = node.previous
        gc.collect()

    def traverse(self):
        tmp = self.head
        res = []
        while tmp:
            res.append(tmp.value)
            tmp = tmp.next
        return res
