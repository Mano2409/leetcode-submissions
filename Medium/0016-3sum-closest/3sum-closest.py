class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        ans=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]      
                if abs(ans-target)>abs(sum-target):
                    ans=sum
                if sum==target:
                    return target
                if sum>target:
                    right-=1
                else:
                    left+=1
        return ans  