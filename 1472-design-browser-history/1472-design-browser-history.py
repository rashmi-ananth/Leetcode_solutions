class Node:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(None, homepage, None)
        self.curr = self.head
        
    def visit(self, url: str) -> None:
        node = Node(self.curr, url, None)
        self.curr.next = node
        self.curr = node

    def back(self, steps: int) -> str:
        
        while self.curr.prev != None and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
            
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next != None and steps > 0:
            self.curr = self.curr.next
            steps -= 1
            
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)