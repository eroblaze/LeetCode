from collections import Counter

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # [[0,1], [0,2], [1,1]]
        # make a dict of each user and their UAM
        all_logs = {}
        for log in logs:
            key = all_logs.setdefault(log[0], set())
            key.add(log[1])
            
        c = [len(val) for (key,val) in all_logs.items()]    
        count = dict(Counter(c))
        result = [0] * k
        for (key, val) in count.items():
            result[key-1] = val
            
        return result
