from random import randint
class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.dictionary = defaultdict(list)
        

    def insert(self, val: int) -> bool:
        self.dictionary[val].append(len(self.list))
        self.list.append(val)
        return len(self.dictionary[val]) == 1
        

    def remove(self, val: int) -> bool:
        # print('rem')
        # print(self.list, self.dictionary)
        if val not in self.dictionary.keys() or len(self.dictionary[val]) == 0:
            return False
        
        idx = self.dictionary[val].pop()
        last = self.list[-1]
        self.list[idx] = last
        self.dictionary[last].append(idx)
        self.dictionary[last].remove(len(self.list) - 1)
        self.list.pop()
        # print(self.list, self.dictionary)
        
        return True
        
        

    def getRandom(self) -> int:
        val = randint(0, len(self.list) - 1)
        return self.list[val]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()