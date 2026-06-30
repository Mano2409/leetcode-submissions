class Solution:
    def finalString(self, s: str) -> str:
    
        k=""
        for j in range(len(s)):
            if s[j]!="i":
                k+=s[j]


            if s[j]=="i":

                k=k[::-1]
        return "".join(k)
