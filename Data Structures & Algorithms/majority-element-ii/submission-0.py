class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = int(len(nums)/3)

        count = Counter(nums)
        res = []
        for i , j in count.items():
            if j > n:
                res.append(i)

        return res
        