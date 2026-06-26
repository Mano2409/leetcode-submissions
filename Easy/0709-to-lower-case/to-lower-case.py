class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                res += chr(ord(ch) + 32)
            else:
                res += ch

        return res