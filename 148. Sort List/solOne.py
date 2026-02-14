

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

    def merge(self,rightll,leftll):
        dummy = Node(0)
        temp = dummy
        while rightll and leftll:
            if rightll.val > leftll.val:
                temp.next = leftll
                leftll = leftll.next
            else:
                temp.next = rightll
                rightll = rightll.next

            temp = temp.next
        
        if rightll:
            temp.next = rightll
        else:
            temp.next = leftll

        return dummy.next


    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        rightnode = mid.next
        mid.next = None
        rightll = self.sortList(rightnode)
        leftll = self.sortList(head)

        return self.merge(rightll,leftll)

    def getMid(self,node):
        slow = node
        fast = node
        while fast and fast.next and  fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow



if __name__ == "__main__":
    head = [4,2,1,3]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    ll.print(ll.sortList(ll.head))
    