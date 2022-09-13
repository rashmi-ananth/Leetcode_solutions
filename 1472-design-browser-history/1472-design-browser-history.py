

# start<->leetcode<->end
# curr = leetcode
# visit
# curr.next = new site
# new site.prev = curr
# new site.next = end
# end.prev = new site

class Node:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = Node(None, "start", None)
        self.end = Node(self.start, "end", None)
        self.start.next = self.end
        
        homepage_node = Node(self.start, homepage, self.end)
        self.end.prev = homepage_node
        self.start.next = homepage_node
        
        self.curr = homepage_node

    def visit(self, url: str) -> None:
        new_page = Node(self.curr, url, self.end)
        new_page.next.prev = new_page
        new_page.prev.next = new_page
        
        self.curr = new_page
          
    def back(self, steps: int) -> str:
        
        while steps > 0:
            if self.curr.prev.val == "start":
                break
            self.curr = self.curr.prev    
            steps -= 1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next.val == "end":
                break
            self.curr = self.curr.next    
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)