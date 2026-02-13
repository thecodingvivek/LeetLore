class Node:
    def __init__(self, value):
        self.value = value
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
            print(temp.value)
            temp = temp.next


    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head

        if  not head or not head.next :
            return False
        fast = head.next.next
        slow = head.next
        while slow != fast:
            if not fast or  not fast.next or not slow or  not slow.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
            

ll = LinkedList(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)

# ll.print(ll.head)
ll.print(ll.head)

print(ll.hasCycle(ll.head))