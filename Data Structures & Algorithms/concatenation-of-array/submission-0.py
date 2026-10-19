class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # return nums+nums
        # return 2* nums
        # return 2*[k for k in nums]
        return 2*[nums[i] for i in range(len(nums))]


        