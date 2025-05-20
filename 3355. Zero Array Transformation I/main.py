class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        decrements = [0] * (n + 1)

        for query in queries:
            l = query[0]
            r = query[1]
            decrements[l] += 1
            decrements[r + 1] -= 1
        
        decrement_count_for_ith_number = 0
        for i in range(n):
            decrement_count_for_ith_number += decrements[i]
            num_decrements_to_make_for_ith_number = nums[i]
            if num_decrements_to_make_for_ith_number > decrement_count_for_ith_number:
                return False

        return True
