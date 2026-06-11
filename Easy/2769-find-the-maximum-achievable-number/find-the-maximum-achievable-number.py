class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x=num

        for i in range(t):
            num=x+1
            x=num+1

        return x
