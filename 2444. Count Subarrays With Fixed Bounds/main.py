class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        n = len(nums)

        subarrays_with_fixed_bounds = 0

        l = -1
        r = 0
        min_idx = -1
        max_idx = -1
        while (r < n):
            
            if nums[r] > maxK or nums[r] < minK:
                l = min_idx = max_idx = r

            else:
                if(nums[r] == minK):
                    min_idx = r
                if(nums[r] == maxK):
                    max_idx = r
                
                if min_idx < max_idx:
                    subarrays_with_fixed_bounds += min_idx - l
                else:
                    subarrays_with_fixed_bounds += max_idx - l

            r += 1
        
        return subarrays_with_fixed_bounds
