class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''
This function checks if there is a cycle in a linked
list, if there is return True, otherwise return False
'''


def has_cycle(head: Node) -> bool:
    if not(head):
        return head

    slow = head
    fast = head.next

    while slow and fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False
