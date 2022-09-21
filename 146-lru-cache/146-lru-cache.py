class Node:
    def __init__(self, prev, key, val, next):
        self.prev = prev
        self.key = key
        self.val = val
        self.next = next
    

class LRUCache:
    def __init__(self, capacity: int):
        self.LRU = Node(None, 0, "LRU", None)
        self.MRU = Node(self.LRU, 0, "LRU", None)
        self.LRU.next = self.MRU
        
        self.dictionary = dict()

        self.counter = 0
        self.capacity = capacity
    
        
    def get(self, key: int) -> int:

        if key in self.dictionary.keys():

            # remove curr node
            node = self.dictionary[key]
            temp = node.next
            node.prev.next = temp
            temp.prev = node.prev
            
            # add curr node to front
            self.add_node(node)
            return self.dictionary[key].val
        else:
            return -1
    
    def add_node(self, node):
        temp = self.MRU.prev
        temp.next = node
        node.prev = temp
        node.next = self.MRU
        self.MRU.prev = node   

    def put(self, key: int, value: int) -> None:
        
        if key in self.dictionary.keys():
            
            # update curr node val
            # remove curr node
            self.dictionary[key].val = value
            node = self.dictionary[key]
            temp = node.next
            node.prev.next = temp
            temp.prev = node.prev
            
            # add curr node to front
            self.add_node(node)
        
        # if key not in dict and c < c
        else: 
            if self.counter < self.capacity:
               
                self.counter += 1   

            else:
                temp = self.LRU.next
                self.LRU.next = temp.next
                temp.next.prev = self.LRU
                del self.dictionary[temp.key]

        
            node = Node(None, key, value, None)
            self.add_node(node)
            self.dictionary[key] = node 
        

            

    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)