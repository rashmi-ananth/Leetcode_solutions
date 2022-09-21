from random import randint
class RandomizedSet:

    def __init__(self):
        self.dictionary = dict()
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.dictionary.keys():
            return False
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dictionary.keys():
            self.list.remove(val)
            del self.dictionary[val]
            return True
        return False
        

    def getRandom(self) -> int:
        val = randint(0, len(self.list) -1)

        return self.list[val]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()