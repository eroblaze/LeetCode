class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        n = 0
        for i in words:
            if s.startswith(i):
                n += 1
                
        return n