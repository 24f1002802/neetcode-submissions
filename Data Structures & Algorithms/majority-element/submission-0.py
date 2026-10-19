class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        t = len(nums)//2

        count = Counter(nums)
        for num, freq in count.items():
            if freq > t:
                return num

            
        