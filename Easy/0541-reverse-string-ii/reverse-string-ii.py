class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        start = 0

        while start < len(arr):
            left = start
            right = start + k - 1

            if right >= len(arr):
                right = len(arr) - 1

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            start += 2 * k

        return "".join(arr)