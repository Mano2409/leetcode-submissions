class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = 0
        less = []
        equal = []
        greater = []

        while left < len(nums):
            if nums[left] < pivot:
                less.append(nums[left])
                left += 1
            elif nums[left] == pivot:
                equal.append(nums[left])
                left += 1
            else:
                greater.append(nums[left])
                left += 1

        return less + equal + greater