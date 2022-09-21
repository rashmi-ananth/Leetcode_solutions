from heapq import heapify, heappush, heappop
class Leaderboard:

    def __init__(self):
        self.dictionary = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.dictionary.keys():
            self.dictionary[playerId] += score
        else:
            self.dictionary[playerId] = score
            
    def top(self, K: int) -> int:
        
        h = []
        dictionary_items = list(self.dictionary.items())
        i = 0
        while i < K:
            heappush(h, (dictionary_items[i][1], dictionary_items[i][0]))
            i += 1
            
        while i < len(dictionary_items):
            if dictionary_items[i][1] > h[0][0]:
                heappop(h)
                heappush(h, (dictionary_items[i][1], dictionary_items[i][0]))
            i += 1
         
        
        total = 0
        for i in range(len(h)):
            total += h[i][0]
        return total
            
    

    def reset(self, playerId: int) -> None:
        
        self.dictionary[playerId] = 0
        del self.dictionary[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)