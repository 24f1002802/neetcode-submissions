class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        result = []
        for i, j in d.items():
            if j >=k:
                result.append(i)
            
        return result