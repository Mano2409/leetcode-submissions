class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()
        n=len(k)
        left=0
        while left<n:
            word=list(k[left])
            nn=len(word)
            l=0
            r=nn-1
            while l<r:
                word[l],word[r]=word[r],word[l]
                l+=1
                r-=1
            k[left]="".join(word)
            left+=1
        return " ".join(k)