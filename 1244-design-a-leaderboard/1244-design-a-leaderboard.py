from heapq import heapify, heappush, heappop
class Leaderboard:

    def __init__(self):
        self.lb = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.lb[playerId] += score

    def top(self, K: int) -> int:
        h = []
        heapify(h)
        
        
        for v in self.lb.values():
            heappush(h, v)
            if len(h) > K:
                heappop(h)
        
        total = 0
        for i in range(K):
            total += heappop(h)
        
        return total

    def reset(self, playerId: int) -> None:
        self.lb[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)