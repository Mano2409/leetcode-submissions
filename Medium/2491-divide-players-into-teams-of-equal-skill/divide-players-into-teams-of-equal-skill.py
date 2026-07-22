class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        hash_set = []
        skill.sort()
        left = 0
        right = len(skill) - 1
        ans = 0

        while left < right:

            k = skill[left] + skill[right]

            if len(hash_set) == 0:
                hash_set.append(k)
                ans += skill[left] * skill[right]
                left += 1
                right -= 1

            elif k in hash_set:
                ans += skill[left] * skill[right]
                left += 1
                right -= 1

            else:
                return -1

        return ans