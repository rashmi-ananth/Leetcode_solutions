from heapq import heapify, heappush, heappop
class Leaderboard:

    def __init__(self):
        self.dictionary = defaultdict(int)
        
    
    def addScore(self, playerId: int, score: int) -> None:
        self.dictionary[playerId] += score
 
    def top(self, K: int) -> int:
        h = []
        idx = 0
        items_lst = list(self.dictionary.items())
        for key, value in items_lst:
            heappush(h, (value, key))
            idx += 1
            if idx == K:
                break
        while idx < len(items_lst):
            if items_lst[idx][1] > h[0][0]:
                heappop(h)
                heappush(h, (items_lst[idx][1], items_lst[idx][0]))
            idx += 1

        total = 0
        for i in range(K):
            total += h[i][0]
        return total

    def reset(self, playerId: int) -> None:
        del self.dictionary[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)