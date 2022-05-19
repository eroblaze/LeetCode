class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        s_num = ""
        
        for i in s:
            s_num += str(alphabets.index(i) + 1)
            
        s_num = str(s_num)   
        
        for i in range(k):
            temp = sum([int(j) for j in s_num])
            s_num = str(temp)
        
        return s_num