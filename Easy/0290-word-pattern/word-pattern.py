class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
 
        ss={}
        k=[ i for i in pattern]
        s=s.split()
        con=0
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if k[i] not in ss and s[i] not in ss.values():
                ss[k[i]]=s[i]
                con+=1
            elif k[i] in ss:
               if  ss[k[i]] == s[i]:
                con+= 1
        return con==len(s)
        