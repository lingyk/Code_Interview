class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def SortList(self, head:Node):
        if not head:
            return None
        arr = []
        
        while head:
            arr.append(head)
            head = head.next
        arr.sort(key=lambda x:x.val)
        for i in range(1, len(arr)):
            arr[i-1] = arr[i].next
        arr[-1].next = None
        return arr[0]
print(Solution().SortList([4, 2, 3, 1]))
