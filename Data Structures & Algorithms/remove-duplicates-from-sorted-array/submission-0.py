class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = sorted(set(nums))
        n = len(seen)
        nums[:n] = seen
        return len(seen)     