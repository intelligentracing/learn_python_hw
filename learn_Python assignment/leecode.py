def deleteNode(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    value = 0
    for i in head:
        if i == val:
            head.pop(head[value + 1])
        else:
            value += 1
    return head

print(deleteNode([4,5,1,3], 5))