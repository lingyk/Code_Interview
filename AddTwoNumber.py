
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumber(self, l1, l2):
        return TwoNumberHelper(self, l1, l2, 0)
    def TwoNumberHelper(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        result = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            result.next = self.TwoNumberHelper(l1.next, l2.next, c)
        elif c:
            result.next = Node(c)
        return result


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)