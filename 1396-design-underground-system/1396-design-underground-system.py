class UndergroundSystem:

    def __init__(self):
        self.check_in_data = dict()
        self.store_journey = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        difference = t - self.check_in_data[id][1]
        if (self.check_in_data[id][0], stationName) in self.store_journey:
            self.store_journey[(self.check_in_data[id][0], stationName)][0] += difference
            self.store_journey[(self.check_in_data[id][0], stationName)][1] += 1
        else:
            self.store_journey[(self.check_in_data[id][0], stationName)] = [difference, 1]


        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        return self.store_journey[(startStation, endStation)][0] / self.store_journey[(startStation, endStation)][1]
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)





# checkin:
    
#     45: ("leyton", 3)
#     32: ("paradise", 8)
#     27: ("Leyton", 10)
    
    
    
    
# checkout:
    
#     45: ("Waterloo", 15)
#     27: ("Waterloo", 20)
#     32: ("Cambridge", 22)
    
    
    
# avg:
    
#     ("Leyton", "Waterloo"): (total=22, count=2)
#     ("Paradise", "Cambridge"): (total=14, count=1)
    
    
    
    

















