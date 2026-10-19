class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # using for loop
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return sorted([i,j])

        # using enumerate

        for i, v in enumerate(nums):
            for j, w in enumerate(nums[i+1:]):
                if v+ w == target:
                    return[i, j+i+1]

                    
        