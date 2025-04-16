from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        l = 0
        pair_count = 0
        num_good_subarrays = 0

        frequencies = defaultdict(int)
        n = len(nums)

        for r in range(n):
            pair_count += frequencies[nums[r]]
            frequencies[nums[r]] += 1

            while pair_count >= k:
                num_good_subarrays += n - r
                frequencies[nums[l]] -=1
                pair_count -= frequencies[nums[l]]
                l += 1

        return num_good_subarrays
