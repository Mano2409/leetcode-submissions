class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        coun=0
        for i in costs:
            if i<=coins:
                coins-=i
                coun+=1
            else:
                break
        return coun