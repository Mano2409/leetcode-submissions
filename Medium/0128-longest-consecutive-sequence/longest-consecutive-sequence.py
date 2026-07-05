class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        maxeee = 0
        for n in numset:          # <-- iterate over the SET, not nums
            if (n - 1) not in numset:
                leng = 0
                while (n + leng) in numset:
                    leng += 1
                maxeee = max(maxeee, leng)
        return maxeee