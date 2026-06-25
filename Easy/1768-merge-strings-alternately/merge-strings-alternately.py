
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # we need a pointer for the first word
        counter = 0

        #store the result in a list
        res = []

        # loop till we've finished the first word
        while counter < len(word1) or counter < len(word2):

            # if we're at word1, append it
            if counter < len(word1):
                res.append(word1[counter])
            
            if counter < len(word2):
                res.append(word2[counter])
            
            counter += 1

        return ''.join(res)
            




        