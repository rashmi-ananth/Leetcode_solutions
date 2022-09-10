class Node:
    def __init__(self, id, val, next):
        self.id = id
        self.val = val
        self.next = next
    
class OrderedStream:

    def __init__(self, n: int):
        self.dummy = Node(0, "dummy", None)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        
        curr1 = self.dummy
        curr2 = self.dummy.next
        
        while curr2 and curr2.id < idKey:
            curr1 = curr2
            curr2 = curr2.next
        
        curr1.next = Node(idKey, value, curr2)
        
        result = []
        
        while self.dummy.next and self.dummy.next.id == self.ptr:
            result.append(self.dummy.next.val)
            self.dummy.next = self.dummy.next.next
            self.ptr += 1
            
            
  
        
        return result
        
        
            
        
        
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)