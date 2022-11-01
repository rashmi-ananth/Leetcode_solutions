from random import randint
class RandomizedSet:

    def __init__(self):
        self.dictionary = dict()
        self.lst = []
        self.counter = 0

    def insert(self, val: int) -> bool:
        if val not in self.dictionary.keys():
            self.dictionary[val] = self.counter
            self.counter += 1
            self.lst.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.dictionary.keys():
            return False
        if val != self.lst[-1]:
            remove_idx = self.dictionary[val]
            new_val = self.lst[-1]
            self.lst[remove_idx] = new_val
            self.dictionary[new_val] = remove_idx
            del self.dictionary[val]
            self.lst.pop()
        else:
            self.lst.pop()
            del self.dictionary[val]
          
        self.counter -= 1
        return True
            
        

    def getRandom(self) -> int:
        val = randint(0, self.counter - 1)
        return self.lst[val]


        # dictionary: {val:idx}
        #     {1:0,2:1,3:2,4:3}
        # list = [1,2,3,4]
        # if remove val is not last idx
        # replace remove val w last val
        # remove the remove val from dict
        # update new val's idx
       
 
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()