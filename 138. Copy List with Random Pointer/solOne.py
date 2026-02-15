

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


    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ll = Node(0)
        newnode = ll
        d = {None:None}

        node = head
        while node:
            newnode.next = Node(node.val)
            newnode = newnode.next
            d[node] = newnode
            node = node.next
        
        again = head
        againnode = ll.next
        while again:
            againnode.random = d[again.random]
            againnode = againnode.next
            again = again.next
        
        return ll.next




if __name__ == "__main__":
    head = [4,2,1,3]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    ll.print(ll.copyRandomList(ll.head))