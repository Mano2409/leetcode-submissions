class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        for i in range(k):
            if blocks[i]=="W":
                count+=1
        res=count
        pointer=k
        while pointer<len(blocks):
            if blocks[pointer-k]=="W":
                count-=1
            if blocks[pointer]=="W":
                count+=1
            res=min(res,count)
            pointer+=1
        return res 
        