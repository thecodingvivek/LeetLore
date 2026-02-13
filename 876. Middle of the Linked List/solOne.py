# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getLen(head)
        mid = length//2
        
        c=0
        node = head
        while node:
            if c == mid:
                return node

            node=node.next
            c+=1
                


    def getLen(self,head):
        node = head
        count = 0
        while node:
            count+=1
            node = node.next
        
        return count
            

