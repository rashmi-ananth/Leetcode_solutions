from heapq import heapify, heappush, heappop
class Leaderboard:

    def __init__(self):
        self.dictionary = defaultdict(int)
    

    def addScore(self, playerId: int, score: int) -> None:
        self.dictionary[playerId] += score
        
        

    def top(self, K: int) -> int:
   
        sorted_items = sorted(self.dictionary.items(), key=lambda x: -x[1])[:K]
        total = 0

        for i in range(K):
            total += sorted_items[i][1]
        

        return total
        
        

    def reset(self, playerId: int) -> None:
        del self.dictionary[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)