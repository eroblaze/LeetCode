class Solution:
    def largestGoodInteger(self, num: str) -> str:
        matches = []
            
        prev = ""
        
        for i in range(len(num)):
            if len(prev) < 3:
                if not prev:
                    prev += num[i]
                    print(prev)

                if i != len(num)-1:
                    if num[i+1] == prev[-1]:
                        prev += num[i+1]
                    else:
                        prev = num[i+1]
                
            else:
                matches.append(prev)
                prev = ""
                
        if not matches: return ""
        print(matches)
        
        matches = [int(i[0]) for i in matches]
        return str(max(matches)) * 3
            