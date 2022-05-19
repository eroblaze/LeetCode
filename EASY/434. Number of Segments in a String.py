import re

class Solution:
    def countSegments(self, s: str) -> int:
        regex = re.compile(r"[^\s]+")
        match = regex.findall(s)
        return len(match)