import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile(r"[\W_]")
        match = regex.findall(s)
        new_string = regex.sub("", s).lower()
        print(new_string)
        return new_string == new_string[::-1]
        