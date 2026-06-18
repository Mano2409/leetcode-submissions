class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        left = 0
        right = len(k) - 1
        while left < right:
            k[left], k[right] = k[right], k[left]
            left += 1
            right -= 1
        return " ".join(k)
                