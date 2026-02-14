

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
            print(temp.val,end = "->")
            temp = temp.next
        print("end")


    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if not head.next:
            head = None
            return head

        prev.next = slow.next
        return head




if __name__ == "__main__":
    head = [2]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.deleteMiddle(ll.head))
    