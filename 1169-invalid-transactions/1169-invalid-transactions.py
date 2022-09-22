class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        ans, dict1 = set(), defaultdict(set)
        for i, info in enumerate(transactions):
            name, time, amount, city = info.split(',')
            if int(amount) > 1000:
                ans.add(i)
                
            for j, t, c in dict1[name]:
                if city != c and abs(t - int(time)) <= 60:
                    ans.add(j)
                    ans.add(i)
                    
            dict1[name].add((i, int(time), city))
        
        return_lst = []
        for i in ans:
            return_lst.append(transactions[i])
                    
        return return_lst
        
        
        
        

#         for i, inf in enumerate(transactions):
#             name, time, amount, city = inf.split(",")

#             if int(amount) > 1000:
#                 ans.add(i)

#             for j, t, c in dict1[name]:
#                 if c != city and abs(int(t) - int(time)) <= 60:
#                     ans.add(j)
#                     ans.add(i)

#             dict1[name].add((i, time, city))

#         return [transactions[i] for i in ans]
                
            