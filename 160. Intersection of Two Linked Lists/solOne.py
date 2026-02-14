

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


    def getIntersectionNode(self, headA, headB):
        fcount = self.getLen(headA)
        scount = self.getLen(headB)
        nodeA = headA
        nodeB= headB
        diff = abs(fcount - scount)
        count = 0
        if fcount > scount:
            for  i in range(diff):
                nodeA = nodeA.next
        else:
            for  i in range(diff):
                nodeB = nodeB.next

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return None

        

    def getLen(self,head):
        node = head
        count = 0
        while node:
            count+=1
            node = node.next
        
        return count




if __name__ == "__main__":
    head = [4,2,1,3]
    ll = LinkedList(head[0])
    for i in range(1,len(head)):
        ll.insert(head[i])

    ll.print(ll.head)
    