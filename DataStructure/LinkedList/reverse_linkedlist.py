class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(node):
    current = node
    prev = None
    next = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
