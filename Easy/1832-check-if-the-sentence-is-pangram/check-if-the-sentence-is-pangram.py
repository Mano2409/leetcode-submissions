class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        hash_table = {}
        for i in sentence:
            hash_table[i] = 1
        return len(hash_table) == 26