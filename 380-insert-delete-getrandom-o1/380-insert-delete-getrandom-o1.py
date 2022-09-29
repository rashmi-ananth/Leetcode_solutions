from random import randint
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dictionary = dict()
        
    def insert(self, val: int) -> bool:
        if val in self.dictionary.keys():
            return False
        
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dictionary.keys():
            return False
        # remove
        idx = self.dictionary[val]
        last_val = self.list[-1]
        self.list[idx] = last_val
        self.dictionary[last_val] = idx
        del self.dictionary[val]
        self.list.pop()
        return True


    def getRandom(self) -> int:
        val = randint(0, len(self.list) - 1)
        return self.list[val]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()