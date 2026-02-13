class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert(self, value):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = ListNode(value)

    def delete(self,value):
        temp=self
        while temp:
            if temp.next == None:
                return 

            if temp.val == value:
                print(value)
                temp.val = temp.next.val
                temp.next = temp.next.next
            temp = temp.next

    def print(self):
        temp = self
        while temp:
            print(temp.val)
            temp = temp.next



arr = [4, 5, 1, 9]
head = ListNode(arr[0])
for i in range(1, len(arr)):
    head.insert(arr[i])


