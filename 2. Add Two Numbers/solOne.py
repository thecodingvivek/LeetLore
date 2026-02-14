

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


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rem = 0
        newnode = ListNode(0)
        result = newnode
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            sums = l1.val + l2.val + rem
            rem = int(sums/10)
            result.next = ListNode(int(sums%10))
            l1 = l1.next
            l2 = l2.next
            result = result.next
        
        if rem > 0:
            result.next = ListNode(rem)

        return newnode.next




if __name__ == "__main__":
    head = [4,2,1,3]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    