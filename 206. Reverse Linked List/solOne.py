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

    def reverseList(self, head):
        temp = head
        prevnode = None

        while temp:
            nextnode = temp.next
            temp.next = prevnode
            prevnode = temp
            temp = nextnode


        head = prevnode
        return head


ll = LinkedList(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)

# ll.print(ll.head)
ll.head = ll.reverseList(ll.head)
print("----")

ll.print(ll.head)