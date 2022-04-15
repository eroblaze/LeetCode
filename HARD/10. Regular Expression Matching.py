import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = re.compile("^"+p+"$")
        match = regex.match(s)
        if (match): return True
        return False
       