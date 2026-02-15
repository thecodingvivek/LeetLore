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

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        count = 1
        node = head

        while node and count <=k:
            prev = node
            node = node.next
            count+=1
        
        if count <= k:
            return head

        prev.next = None

        lls = self.reverse(head)
        head.next = self.reverseKGroup(node,k)

        return lls

    def reverse(self,head):
        node = head
        prev = None
        while node:
            nextnode = node.next
            node.next = prev
            prev = node
            node = nextnode
        return prev

        




if __name__ == "__main__":
    head = [1,2,3,4,5]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    ll.print(ll.reverseKGroup(ll.head,3))
    