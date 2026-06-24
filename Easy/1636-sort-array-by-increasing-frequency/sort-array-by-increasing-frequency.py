class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        List = {}

        for i in range(len(nums)):
            List[nums[i]] = List.get(nums[i], 0) + 1

        sortedd = sorted(List.items(), key=lambda x: (x[1], -x[0]))

        res = [x for x, y in sortedd for i in range(y)]

        return res