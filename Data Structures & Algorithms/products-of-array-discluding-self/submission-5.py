class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * postfix
            postfix = postfix * nums[i]
        return ans
        
        # n = len(nums)
        # res = [1] * n

        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]

        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     res[i] *= suffix
        #     suffix *= nums[i]

        # return res

