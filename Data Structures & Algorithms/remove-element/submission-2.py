class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0

        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1       
        # return k

        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        counter = 0

        for num in nums:
            if val == num:
                counter += 1

        for i in range(counter):
            nums.remove(val)
            
        return len(nums)
        