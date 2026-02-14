# 10->11->12->13
# 10->12->13->11

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


    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return 
        odd = head
        even = head.next
        evenhead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenhead
        return head
                                

ll = LinkedList(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

ll.print(ll.oddEvenList(ll.head))
