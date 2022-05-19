import re

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        using their ascii codes
        """
        regex = re.compile(r"^(?P<main>(?:.+)://.+\.[^/]+/)(.*)", re.I)
        
        mainMatch = regex.findall(longUrl)
        match = mainMatch[0][1]
        
        m2 = mainMatch[0][0]
        
        if match: 
            encodedstring = "-".join([str(ord(i)) for i in match])
            tiny = m2 + encodedstring
            return tiny
        return m2
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        decode using chr()
        """
        regex = re.compile(r"^(?P<main>(?:.+)://.+\.[^/]+/)(.*)", re.I)
        
        mainMatch = regex.findall(shortUrl)
        match = mainMatch[0][1].split("-") if mainMatch[0][1] else ""
        m2 = mainMatch[0][0]
        
        if match: 
            decodedstring = "".join([chr(int(i)) for i in match])
            long = m2 + decodedstring
            return long
        return m2

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))