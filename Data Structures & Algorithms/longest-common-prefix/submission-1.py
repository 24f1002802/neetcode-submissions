class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #using enumerates

        first_word = strs[0]
        lcp = ""
        check_all = True

        for i, c in enumerate(first_word):
            for word in strs:
                if word[i] != c:
                    return lcp
            lcp += c
        return lcp