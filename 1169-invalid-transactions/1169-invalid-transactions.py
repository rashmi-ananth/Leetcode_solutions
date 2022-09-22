class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        names = defaultdict(list)
        arr = []
        invalid = set()
        for i in transactions:
            arr.append(i.split(','))
        
        for i in range(len(arr)):
            if int(arr[i][2]) > 1000:
                invalid.add(','.join(arr[i]))
                
            city = arr[i][-1]
            time = int(arr[i][1])
            for j in range(len(names[arr[i][0]])):
                if city != names[arr[i][0]][j][-1] and abs(time - int(names[arr[i][0]][j][1])) <= 60:
                    
                    invalid.add(','.join(arr[i]))
                    invalid.add(','.join(names[arr[i][0]][j]))
                    
                
                
            names[arr[i][0]].append(arr[i])
         
        return_lst = []
        
        for i in transactions:
            if i in invalid:
                return_lst.append(i)
                
        return return_lst
                
            