class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # iteration approach 
        return Counter(s) == Counter(t)
        