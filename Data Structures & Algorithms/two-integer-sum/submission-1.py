class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # using for loop
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return sorted([i,j])

        # using list

        lst = []

        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i + j == target:
                    lst.append(nums.index(i))
                    lst.append(nums.index(j))
        return sorted(lst)
                    
        