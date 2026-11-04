class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1

        return -1
        

    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next = self.head
        self.head = newnode

        if self.tail is None:
            self.tail = newnode
        
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newnode = ListNode(val)
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode
        self.tail = newnode
        self.size +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        count = 0
        cur = self.head

        while cur:
            if count == index - 1:
                newnode = ListNode(val)
                newnode.next = cur.next
                cur.next = newnode
                self.size +=1
                return
            cur = cur.next
            count +=1



    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None
            return
        
        count = 0
        cur = self.head

        while cur.next:
            if count == index - 1:
                cur.next = cur.next.next
                if index == self.size - 1:
                    self.tail = cur
                self.size -= 1
                return
            count +=1
            cur = cur.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)