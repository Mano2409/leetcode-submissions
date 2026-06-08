class Solution(object):
    def twoSum(self, nums, target):
        s={}
        for i in range(len(nums)):
            if target-nums[i] in s:
                return [i,s[target-nums[i]]]

            s[nums[i]]=i
        