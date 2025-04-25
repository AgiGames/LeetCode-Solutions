from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        n = len(nums)
        cache = defaultdict(int)
        cache[0] = 1
        result = 0
        prefix = 0

        for i in range (n):
            prefix += ((nums[i] % modulo) == k)
            result += cache[(prefix + modulo - k) % modulo]
            cache[prefix % modulo] += 1

        return result
