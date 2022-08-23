class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        # Initialize dictionary
        hashmap = dict()
        hashmap['c'] = 0
        hashmap['r'] = 0
        hashmap['o'] = 0
        hashmap['a'] = 0
        hashmap['k'] = 0
        

        total = 0
        
        # Iterate through chars
        for i in range(len(croakOfFrogs)):
            hashmap[croakOfFrogs[i]] += 1
            
            if croakOfFrogs[i] == 'c':
                if total > 0:
                    total -= 1
            
            if croakOfFrogs[i] == 'k':
                total += 1
              
            if (hashmap['c'] < hashmap['r'] or hashmap['r'] < hashmap['o'] or hashmap['o'] < hashmap['a'] or hashmap['a'] < hashmap['k']): 
                
                return -1
            
        if hashmap['c'] == hashmap['r'] == hashmap['o'] == hashmap['a'] == hashmap['k']:
            return total
        
        return -1
        
            
           
            
            
        