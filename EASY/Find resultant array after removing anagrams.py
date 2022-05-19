class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1: return words
        words_cpy = words[:]
        not_anag = []        
        
        while len(words_cpy) > 1:
            first, sec = "".join(list(sorted(list(words_cpy[0])))), "".join(list(sorted(list(words_cpy[1]))))
            
            if first == sec:
                words_cpy.pop(1)
            else: not_anag.append(words_cpy.pop(0))

        not_anag.append(words_cpy.pop(0))
        
        return not_anag