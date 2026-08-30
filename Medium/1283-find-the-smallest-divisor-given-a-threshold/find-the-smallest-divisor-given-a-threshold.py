class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=max(nums)
        while low<=high:
            mid=(low+high)//2
            final=self.func(nums,mid)
            if final<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans




   
    def func(self,nums,mid):
        total=0
        for i in nums:
            total+=math.ceil(i/mid)
        return total