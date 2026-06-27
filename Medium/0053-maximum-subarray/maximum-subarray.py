class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxee=nums[0]
        counte=0
        for x in nums:
            counte+=x
            maxee=max(maxee,counte)

            if counte<0:
                counte=0
        return maxee