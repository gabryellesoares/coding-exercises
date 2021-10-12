class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = SinglyLinkedListNode


def insertNodeAtPosition(head, data, position):
    if head is None or position == 0:
        return SinglyLinkedListNode(data)

    current = head
    pos = 0

    while pos < position-1:
        current = current.next
        pos += 1

    current.next, current.next.next = SinglyLinkedListNode(data), current.next

    return head
