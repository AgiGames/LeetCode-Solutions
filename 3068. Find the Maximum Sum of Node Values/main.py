from math import inf

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        total_sum = 0
        num_tick_marks = 0
        min_loss_so_far = inf

        for num in nums:
            total_sum += max(num, num ^ k)
            if (num ^ k) > num:
                num_tick_marks += 1
            min_loss_so_far = min(min_loss_so_far, abs(num - (num ^ k)))
        
        if num_tick_marks % 2 == 0:
            return total_sum
        return total_sum - min_loss_so_far
