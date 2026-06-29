class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        coun=0
        for i in patterns:
            if i in word:
                coun+=1
        return coun
