class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #using enumerates

        if not strs:
            return ""

        first_word = strs[0]
        lcp = ""
        check_all = True

        for i, c in enumerate(first_word):
            for word in strs:
                if i >= len(word) or word[i] != c:
                    return lcp
            lcp += c
        return lcp