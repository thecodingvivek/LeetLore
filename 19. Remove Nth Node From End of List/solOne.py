

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self,value):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(value)
        


    def print(self,head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next
        print("-----")


    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        length = self.getLen(self.head)
        target = length - n
        count = 0
        node = head
        if target <0 or target == 0:
            head = head.next
            return head

        while node :
            if count == target-1:
                node.next = node.next.next
            node = node.next
            count += 1

        return head
                
            

    def getLen(self,head):
        node = head
        count=0
        while node:
            count+=1
            node = node.next
        return count
                                

ll = LinkedList(1)

ll.print(ll.removeNthFromEnd(ll.head,1))
