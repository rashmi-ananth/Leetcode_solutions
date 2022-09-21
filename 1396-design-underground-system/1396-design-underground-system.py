class UndergroundSystem:

    def __init__(self):
        
        self.check_in_dict = dict()
        self.trips_dict = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.check_in_dict[id][0]
        total_time = t - self.check_in_dict[id][1]
        if (start_station, stationName) in self.trips_dict.keys():
            new_tuple = (self.trips_dict[(start_station, stationName)][0] + total_time, 1 + self.trips_dict[(start_station, stationName)][1])
            self.trips_dict[(start_station, stationName)] = new_tuple
            
        else:
            self.trips_dict[(start_station, stationName)] = (total_time, 1)
            
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        avg = self.trips_dict[(startStation, endStation)][0] / self.trips_dict[(startStation, endStation)][1]
        return avg
        
        
        
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)