class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            if needle [0:1] in haystack:
                return haystack.index(needle)
    
        return -1