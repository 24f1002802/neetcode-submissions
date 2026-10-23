class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

        res = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            res += prefix_map.get(needed, 0)

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return res