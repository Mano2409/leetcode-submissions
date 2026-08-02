class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str):

        sent1 = sentence2.split()
        sent2 = sentence1.split()

        s1 = list(sent1)
        s2 = list(sent2)

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        left1 = 0
        left2 = 0
        right1 = len(s1) - 1
        right2 = len(s2) - 1

        while left1 <= right1:

            if s1[left1] == s2[left2]:
                left1 += 1
                left2 += 1

            elif s1[right1] == s2[right2]:
                right1 -= 1
                right2 -= 1

            else:
                return False

        return True