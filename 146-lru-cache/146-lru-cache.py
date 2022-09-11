class Node:
    
    def __init__(self, prev, key,val, next):
        self.prev = prev
        self.key = key
        self.val = val
        self.next = next

#         LRU <-> MRU
        
#         counter = 1
#         {2:node(2,1)}
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dictionary = defaultdict(int)
        self.LRU = Node(None, "","start", None)
        self.MRU = Node(None, "", "end", None)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        self.capacity = capacity
        self.counter = 0
        
    def get(self, key: int) -> int:
        # print(key)
        # print(self.dictionary.items())
        # curr = self.LRU
        # while curr != None:
        #     print(curr.key, curr.val)
        #     curr = curr.next
        if key in self.dictionary.keys():
            # print(self.counter)
            node = self.dictionary[key]
            # print(key)
            # print("node key")
            # print(node.key)
            temp = node.next
            node.prev.next = temp
            temp.prev = node.prev
            
            temp2 = self.MRU.prev
            temp2.next = node
            node.prev = temp2
            node.next = self.MRU
            self.MRU.prev = node
            # print('hello')
            # print(self.MRU.prev.key)
     
            return self.dictionary[key].val
        else:
            return -1
        

        

    def put(self, key: int, value: int) -> None:
        # print(key, value)
        # print(self.dictionary.items())
        # curr = self.LRU
        # while curr != None:
        #     print(curr.key, curr.val)
        #     curr = curr.next

        if key in self.dictionary.keys():
            self.dictionary[key].val = value
            node = self.dictionary[key]
            temp = node.next
            node.prev.next = temp
            temp.prev = node.prev
            
            temp2 = self.MRU.prev
            temp2.next = node
            node.prev = temp2
            node.next = self.MRU
            self.MRU.prev = node
        else:
            if self.counter == self.capacity:
                
                # removing old LRU node
                # print(self.LRU.next.key)
                
                temp = self.LRU.next
                self.LRU.next = temp.next
                temp.next.prev = self.LRU
                temp.next = None
                temp.prev = None
                del self.dictionary[temp.key]
            else:
                self.counter += 1
                
            # adding new node
            new_node = Node(None, key, value, None)
            temp = self.MRU.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.MRU
            self.MRU.prev = new_node
            self.dictionary[key] = new_node
        # print(self.dictionary)
                

                
            

                
            
        
   
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)