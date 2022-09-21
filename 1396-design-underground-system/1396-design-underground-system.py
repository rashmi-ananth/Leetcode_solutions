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
            self.trips_dict[(start_station, stationName)] = (self.trips_dict[(start_station, stationName)][0] + total_time, 1 + self.trips_dict[(start_station, stationName)][1])
            
        else:
            self.trips_dict[(start_station, stationName)] = (total_time, 1)
            
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        avg = self.trips_dict[(startStation, endStation)][0] / self.trips_dict[(startStation, endStation)][1]
        return avg
        
        
        

        
        
        
        
#         checkin_dict {id:(stationName, t)}
#         avg_time {(start, end):(total time, count)}
        
        
#         45: ('Leyton', 3) 32: (Paradise, 8) 27:(Leyton, 10)
                    
                    
#         45:(Waterloo, 15)
            
        
#         (Leyton, Waterloo):(12, 1)
            
        
        
        
        
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)