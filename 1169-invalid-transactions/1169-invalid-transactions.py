class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # {n:[[t, city, idx]]}
        
        stored_txns = defaultdict(list)
        invalid = set()
        
        for i in range(len(transactions)):
            n, t, a, c = transactions[i].split(',')
            if int(a) > 1000:
                invalid.add(i)
             
            
            for time, city, idx in stored_txns[n]:
                if city != c:
                    if abs(int(t) - time) <= 60:
                        invalid.add(idx)
                        invalid.add(i)
            
            stored_txns[n].append([int(t), c, i])
            
        
        return_lst = []
        for idx in invalid:
            return_lst.append(transactions[idx])

            
        return return_lst
        
       

        