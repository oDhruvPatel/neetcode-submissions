class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_x = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_x == sorted_t:
            return True
        else:
            return False

#this is O(n log n) bcs sorting of string is O(n log n).