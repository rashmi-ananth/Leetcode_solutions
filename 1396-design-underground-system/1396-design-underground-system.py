class UndergroundSystem:

    def __init__(self):
        self.check_in_dict = dict()
        self.paths = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.check_in_dict[id][0]
        start_time = self.check_in_dict[id][1]
        difference = t - start_time
        
        if (start, stationName) in self.paths.keys():
            self.paths[(start, stationName)][0] += difference
            self.paths[(start, stationName)][1] += 1
        else:
            self.paths[(start, stationName)] = [difference, 1]
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.paths[(startStation, endStation)]
        return total / count
        
        

 



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)