class OrderedStream:

    def __init__(self, n: int):
        self.idx = 1
        self.dictionary = dict()
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dictionary[idKey] = value
        return_lst = []
        
        while self.idx in self.dictionary.keys():
            return_lst.append(self.dictionary[self.idx])
            self.idx += 1
            
        return return_lst
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

