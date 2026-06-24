class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Cs_s = {}
        Cs_t = {}

        for i, char in enumerate(s):
                Cs_s[char] = Cs_s.get(char, 0) + 1
        
        for i, char in enumerate(t):
            Cs_t[char] = Cs_t.get(char, 0) + 1
        
        return Cs_s == Cs_t
