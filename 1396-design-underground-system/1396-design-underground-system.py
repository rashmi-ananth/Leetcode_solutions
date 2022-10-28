class UndergroundSystem:

    def __init__(self):
        self.check_in_dict = dict()
        self.total_dict = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_dict[id]
        diff = t - start_time
        if (start_station, stationName) in self.total_dict.keys():
            self.total_dict[(start_station, stationName)][0] += diff
            self.total_dict[(start_station, stationName)][1] += 1
        else:
            self.total_dict[(start_station, stationName)] = [diff, 1]
                
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_dict[(startStation, endStation)][0] / self.total_dict[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)