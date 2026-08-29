class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            final=self.check(bloomDay,mid,k)
            if final >=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
            
    def check(self,bloomDay,mid,k):
        total=0
        streak=0
        
        for i in bloomDay:
            

            if i<=mid:
                streak+=1
                if streak==k:
                    streak=0
                    total+=1
            else:
                streak=0
        return total
   
        