from random import randint
class RandomizedSet:

    def __init__(self):
        
        self.dictionary = defaultdict(int)
        self.list = []
        

    def insert(self, val: int) -> bool:
  
        if val in self.dictionary.keys():
            return False
        else:
            self.dictionary[val] = len(self.list)
            self.list.append(val)
            # self.last_idx = self.dictionary[val]
            return True
            
    def remove(self, val: int) -> bool:
        # print("remove")
        # print(val)
        # print(self.dictionary, self.list, self.last_idx)
        if val in self.dictionary:
            last_val = self.list[-1]
            idx = self.dictionary[val]
            self.list[idx] = last_val
            self.dictionary[last_val] = idx
            del self.dictionary[val]
            self.list.pop()
            
            
            
            
            # idx = self.dictionary[val]
            # self.dictionary.pop(val)
            # new_val = self.list[self.last_idx]
            # if self.last_idx != 0:
            #     self.list[idx] = new_val
            #     self.list.pop()
            #     self.last_idx -= 1
            #     self.dictionary[new_val] = idx
            # self.last_idx -= 1
            # print(self.dictionary)
            return True

        else:
            return False
        

    def getRandom(self) -> int:
        # print(self.dictionary, self.list, self.last_idx)
        val = randint(0, len(self.list) -1)
        return self.list[val]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()