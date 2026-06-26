class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""
        start = 0
        
        for ch in s:
            if(ch.isalnum()):
                alnum += ch.lower()
        
        end = len(alnum) - 1

        if (len(s) == 0 or len(s) == 1):
            return True

        while(start < end):
            if (alnum[start] != alnum[end]):
                return False
            else:
                start += 1
                end -= 1
        return True