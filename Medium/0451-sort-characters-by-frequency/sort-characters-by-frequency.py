from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1
        freq=sorted(freq.items(),key =lambda x:-x[1])
        return "".join([y*x for y,x in  freq])
