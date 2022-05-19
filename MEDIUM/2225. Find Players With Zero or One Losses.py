class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # first -> not lost, second -> lost only one
        scores = {"winners": set(), "losers": {}}
        res = [[], []]
        
        for i in matches:
            scores["winners"].add(i[0])
            n = scores["losers"].setdefault(i[1], 0)
            scores["losers"][i[1]] += 1  
        
        if (x:=scores["winners"]):
            if (y:=scores["losers"]):
                for i in x:
                    if i not in y.keys():
                        res[0].append(i)
        if (y:=scores["losers"]):
            res[1] = [val for val, count in y.items() if count == 1]

        if res[0]: res[0].sort()
        if res[1]: res[1].sort()
        return res