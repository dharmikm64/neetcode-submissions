# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        myMap = {}

        if head == None:
            return False
        while curr: 
            temp = curr.next
            if curr.next == None:
                return False 
            elif curr.next in myMap:
                return True 
            myMap[curr.next] = 0
            curr = temp 
        return True 