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

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        node = head
        k = k % length

        if k == 0:
            return head

        tail.next = head
        for i in range(length - k-1):
            node = node.next
        
        nhead = node.next
        node.next = None

        return nhead
    

        




if __name__ == "__main__":
    head = [1]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    ll.print(ll.rotateRight(ll.head,2))
    