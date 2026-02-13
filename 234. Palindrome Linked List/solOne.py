# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        i=0
        j = len(nums)-1

        while i<=j:
            if nums[i] != nums[j]:
                return False
            i+=1
            j-=1
        
        return True
        