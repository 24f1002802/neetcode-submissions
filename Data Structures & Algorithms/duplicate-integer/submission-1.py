class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dictionary approach: 1
        # d = dict()
        # for i in nums:
        #     if i in d.keys():
        #         d[i] += 1
        #         if d[i] >1 :
        #             return True
        #     else:
        #         d[i] = 1
        # return False

        # dictionary approach: 2
        # d = dict()
        # for k in nums:
        #     d[k] = d.get(k,0)+1
        #     if d[k] > 1:
        #         return True
        # return False

        # iteration approach

        # count = Counter(nums)

        # for i in count.values():
        #     if i > 1:
        #         return True
        # return False

        # set approach
        # s = set()

        # for i in nums:
        #     if i in s:
        #         return True
        #     else  :  
        #         s.add(i)
        # return False

        return len(set(nums)) != len(nums)
            