class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        

class BrowserHistory:

    def __init__(self, homepage: str):
        newnode = ListNode(homepage)
        self.head = newnode
        self.cur = self.head
        

    def visit(self, url: str) -> None:
        newnode = ListNode(url)
        self.cur.next = newnode
        newnode.prev = self.cur
        self.cur = newnode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev is None:
                break
            self.cur = self.cur.prev

        return self.cur.val


    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next is None:
                break
            self.cur = self.cur.next

        return self.cur.val
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)