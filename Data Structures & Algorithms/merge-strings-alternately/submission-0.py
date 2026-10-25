class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = 0
        n = 0
        s = []

        while m < len(word1) and n < len(word2):
            s.append(word1[m])
            s.append(word2[n])
            m += 1
            n += 1

        s.append(word1[m:])
        s.append(word2[n:])
        return "".join(s)
        