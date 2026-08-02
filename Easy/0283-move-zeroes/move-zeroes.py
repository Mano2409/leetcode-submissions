class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0

        while left <= right:
            if nums[left] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            else:
                left += 1