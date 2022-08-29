def reverseLinkedList(LinkedList node):
    current = node
    prev = None
    next = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev