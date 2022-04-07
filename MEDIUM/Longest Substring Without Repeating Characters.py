class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = "";
        array = [];
        for i in s:
            if i in res:
                array.append(len(res))
                idx = res.index(i)
                if len(res) > 1:
                    res = res[idx+1:] + i
                    print(res)
                else:
                    res = i
            else:
                res += i
                array.append(len(res))
                
        if len(array):
            return max(array)
        return 0
