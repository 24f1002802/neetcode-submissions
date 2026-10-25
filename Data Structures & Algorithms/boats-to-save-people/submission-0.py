class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        s = 0

        while l <= r:

            total = people[l] + people[r] 
            if total <= limit:
                l += 1
                
            r -= 1
            s += 1

        return s 

