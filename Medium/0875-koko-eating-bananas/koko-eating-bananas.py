class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            total=self.func(piles,mid)
            if total<=h:
                ans=mid
                high=mid-1

            else:
                low=mid+1
        return ans
    def func(self,piles,mid):
        final=0
        for i in piles:
            final+=math.ceil(i/mid)
        return final

        