class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        
#     dict: name:[(idx, [t, city]), (idx, [t, city])]
        
#         set: 0,2,5 - result idx

        
        result_idx = set()
        visited_dictionary = defaultdict(list)
        
        for i in range(len(transactions)):
            name, t, amt, city = transactions[i].split(',')
            
            if int(amt) > 1000:
                result_idx.add(i)
                
            for item in visited_dictionary[name]:
                t2 = item[1][0]
                city2 = item[1][1]
                
                if city != city2 and abs(int(t)-t2) <= 60:
                    result_idx.add(i)
                    result_idx.add(item[0])
            visited_dictionary[name].append((i,[int(t), city]))
            
            
        
        result = []
        for i in result_idx:
            result.append(transactions[i])
    
        return result
            
            
        
            
                    
                    
            
                
                
            
            
            
            
            

        



            
            
                
        
        
        