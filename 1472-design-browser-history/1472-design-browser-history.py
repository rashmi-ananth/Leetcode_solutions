class Node:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val
class BrowserHistory:
    

            

    def __init__(self, homepage: str):
        self.head = Node(None, None, homepage)
        

    def visit(self, url: str) -> None:
        node = Node(self.head, None, url)
        self.head.next = node
        self.head = node
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.prev != None:
            steps -= 1
            self.head = self.head.prev
        
        return self.head.val
            
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.next != None:
            steps -= 1
            self.head = self.head.next
        
        return self.head.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)