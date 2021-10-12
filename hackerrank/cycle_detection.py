def has_cycle(head):
    if head is None:
        return 0

    slow = head
    fast = head

    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1

    return 0
