class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])

        for i in range(k, len(arr) + 1):

            # Check current window
            if window_sum >= k * threshold:
                count += 1

            # Move the window
            if i < len(arr):
                window_sum = window_sum - arr[i-k] + arr[i]

        return count