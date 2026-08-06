class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        track = True

        while track:
            product = 1
            copy = n

            while copy != 0:
                digits = copy % 10
                copy = copy // 10
                product *= digits

            if product % t == 0:
                return n
            else:
                n += 1