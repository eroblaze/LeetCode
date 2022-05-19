from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # favour 3 over 2
        # if 3 can enter, try another 3
        # if the other 3 can enter, keep on trying until no more can enter
        # check if 2 can enter with the remainder
        # else backtrack to the previous 3 and check if 2 would have entered
        # if I backtrack back to 0 return [-1]
        
        
        c_dict = dict(Counter(tasks))
        c_dict_val = c_dict.values()
        
        if 1 in c_dict.values(): return -1
        # [2,2,3,3,2,4,4,4,4,4] -> {2: 3, 3: 2, 4: 5} -> [3,2,5]
        # 7
        # 2 r 1
        # 1 = 3 r 4
        count = 0
        for i in c_dict_val:
            # try 3
            if i >= 3:
                if i % 3 == 0:
                    count +=  i // 3
                else:
                    # there is a remainder e.g 7  // 3 -> 2 r 1
                    predicate = i // 3
                    rem = i - (predicate * 3)
                    
                    while predicate > 0 and rem % 2 != 0:
                        predicate -= 1
                        rem = i - (predicate * 3)
                        
                    # predicate is either 0 or predicate > 0
                    if predicate == 0:
                        if i % 2 == 0:
                            count += i // 2
                        else: return -1
                    else:
                        to_add = predicate + (rem // 2)
                        count += to_add
            else:
                # i == 2
                count += i // 2
        
        return count
        
        