class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [None] * self.n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        return_arr = []
        if idKey-1 == self.ptr:
            while self.ptr < self.n and self.arr[self.ptr] != None:
                return_arr.append( self.arr[self.ptr])
                self.ptr += 1
        
        return return_arr
            

            
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)