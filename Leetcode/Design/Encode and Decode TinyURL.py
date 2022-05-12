'''
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
'''

import string
import random

class Codec:
    def __init__(self):
    # alphabet: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        self.alphabet = string.ascii_letters + string.digits
        self.hashMap = {}
        self.candidateURL = self.getRand()

    def getRand(self):
        # loop 6 times, because the length of the code is fixed to 6 only
        shortURL = ''
        for _ in range(6):
            shortURL += self.alphabet[random.randint(0,61)]
        return shortURL

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # While loop here is to prevent collisions with previously generated code
        while self.candidateURL in self.hashMap:
            self.candidateURL = self.getRand()
        self.hashMap[self.candidateURL] = longUrl
        return 'http://tinyurl.com/' + self.candidateURL

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashMap[shortUrl.replace('http://tinyurl.com/','')]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

'''
The number of URLS can be encoded nearly (10+26*2)^6
The length of encoded URLs is fixed to 6 units, significantly reduce for large URLs
Very less probability of repeated same codes generated
We can increase the number of encodings possible as well by increasing the length of the encoded strings
Exist tradeoff between the length of the code and the number of encoings possible
Predicting the encoding is not possible since we are using random numbers
'''
