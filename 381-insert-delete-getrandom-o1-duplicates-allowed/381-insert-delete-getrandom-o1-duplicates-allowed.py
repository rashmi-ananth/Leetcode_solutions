from random import randint
class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.dictionary = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        self.dictionary[val].add(len(self.list))
        self.list.append(val)
        return len(self.dictionary[val]) == 1
        

    def remove(self, val: int) -> bool:
        if val not in self.dictionary.keys():
            return False
        
        idx = self.dictionary[val].pop()
        last = self.list[-1]
        self.list[idx] = last
        self.dictionary[last].add(idx)
        self.dictionary[last].remove(len(self.list) - 1)
        self.list.pop()
        
        if len(self.dictionary[val]) == 0:
            del self.dictionary[val]
        
        return True
        
        

    def getRandom(self) -> int:
        val = randint(0, len(self.list) - 1)
        return self.list[val]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()