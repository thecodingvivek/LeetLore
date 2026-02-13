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
        


    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

ll = LinkedList(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)

ll.print()