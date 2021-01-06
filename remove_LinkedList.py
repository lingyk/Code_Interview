class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def __str__(self):
        n = self
        answer = ''

        while n:
            answer += str(n.val)
            n = n.next
        return answer
    

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    sentinel = Node(0, None)
    sentinel.next = head
    
    curr, prev = head, sentinel
    
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        
        curr = curr.next
    return sentinel.next

head = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6, None)))))))
print(removeElements(head, 6))