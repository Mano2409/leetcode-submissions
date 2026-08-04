class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)

        index = -1
        i = 0
        while i < len(arr):
            if arr[i] == ch:
                index = i
                break
            i += 1

        if index == -1:
            return word

        left = 0
        right = index

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)