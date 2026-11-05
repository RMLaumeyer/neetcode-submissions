class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x: int) -> None:
        newnode = ListNode(x)

        if self.size == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

        self.size += 1
        

    def pop(self) -> int:
        cur = self.head

        if self.size == 1:
            temp = self.head.val
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        for i in range(self.size - 2):
            cur = cur.next

        self.tail = cur
        temp = cur.next.val
        self.tail.next = None
        self.size -= 1

        return temp

        

    def top(self) -> int:
        return self.tail.val
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()