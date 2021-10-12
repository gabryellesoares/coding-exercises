class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    return reverse(None, head)


def reverse(node, nextNode):
    if not nextNode:
        return node

    aux = nextNode.next
    nextNode.next = node
    return reverse(nextNode, aux)
