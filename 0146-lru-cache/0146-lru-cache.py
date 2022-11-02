class Node:
    def __init__(self,prev, next, key, val):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val
    
class LRUCache:
    
    # linked list
    # LRU<->1:1<->2:2<->MRU
    # for efficient access for each of the nodes, include dict

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = Node(None, None, -1, -1)
        self.MRU = Node(self.LRU, None, -1, -1)
        self.LRU.next = self.MRU
        self.dictionary = dict()
        self.counter = 0
        
    def get(self, key: int) -> int:
        # not in cache
        if key not in self.dictionary.keys():
            return -1
        # in cache
        # update in linked list
        node = self.dictionary[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.add_node(node)
        
        return self.dictionary[key].val

    def add_node(self, node):
            prev_node = self.MRU.prev
            self.MRU.prev = node
            node.next = self.MRU
            node.prev = prev_node
            prev_node.next = node
            self.dictionary[node.key] = node

    def put(self, key: int, value: int) -> None:
        # if key in dict
        if key in self.dictionary.keys():
            node = self.dictionary[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            
            self.add_node(node)
            
            node.val = value
            
            return
        else:
            if self.counter == self.capacity:
                remove_node = self.LRU.next
                self.LRU.next = remove_node.next
                remove_node.next.prev = self.LRU
                remove_node.next = None
                remove_node.prev = None
                
                del self.dictionary[remove_node.key] 
            else:
                self.counter += 1
                
            node = Node(None, None, key, value)
            self.add_node(node)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)