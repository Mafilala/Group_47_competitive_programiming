class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self, head = None):
        self.head = head
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        h = self.head
        while index and h:
            h = h.next
            index -= 1
        if index == 0 and h:
            return h.val
        return -1
    def addAtHead(self, val: int) -> None:
        if self.head:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = Node(val)
    def addAtTail(self, val: int) -> None:
        h = self.head
        if not h:
            self.addAtHead(val)
        else:
            while h.next:
                h = h.next
            h.next = Node(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            h = self.head
            while index > 1 and h:
                h = h.next
                index -= 1
            new_node = Node(val)
            if h:
                new_node.next = h.next
                h.next = new_node
    def deleteAtIndex(self, index: int) -> None:
        h = self.head
        if index == 0 and h:
            self.head = h.next
        else:
            while h and index > 1:
                h = h.next
                index -= 1
            if index == 1 and h and h.next:
                h.next = h.next.next
