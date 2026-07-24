class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left = 0
        right = len(s)
        i = 0
        j = len(spaces)
        ans = ""

        while left < right:
            if i < j and left == spaces[i]:
                ans += " "
                i += 1
            else:
                ans += s[left]
                left += 1

        return ans