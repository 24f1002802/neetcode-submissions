class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #using enumerates

        # first_word = strs[0]
        # lcp = ""
        # check_all = True

        # for i, c in enumerate(first_word):
        #     for word in strs:
        #         if i >= len(word) or word[i] != c:
        #             return lcp
        #     lcp += c
        # return lcp


        min_len_word = min(strs, key = len)
        for _ in range(len(min_len_word)):
            for word in strs:
                if not word.startswith(min_len_word):
                    min_len_word = min_len_word[:-1]
                    break
        return min_len_word
