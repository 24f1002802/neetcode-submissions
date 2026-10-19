class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # t = len(nums)//2

        # count = Counter(nums)
        # for num, freq in count.items():
        #     if freq > t:
        #         return num

        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0)+1
            if freq[n] > (len(nums) // 2):
                return n 

            
        