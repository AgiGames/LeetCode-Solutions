class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        l = 0
        r = 0

        nums_set = set(nums)
        num_unique_elements = len(nums_set)
        n = len(nums)

        complete_subarrays = 0

        frequencies = defaultdict(int)
        ith_subarray_set = set()
        while (r < n):
            if len(ith_subarray_set) == num_unique_elements:
                complete_subarrays += n - (r - 1)
                frequencies[nums[l]] -= 1
                if frequencies[nums[l]] == 0:
                    ith_subarray_set.remove(nums[l])
                l += 1
            else:
                ith_subarray_set.add(nums[r])
                frequencies[nums[r]] += 1
                r += 1

        while l < r:
            if len(ith_subarray_set) == num_unique_elements:
                complete_subarrays += n - (r - 1)
            else:
                break
            frequencies[nums[l]] -= 1
            if frequencies[nums[l]] == 0:
                ith_subarray_set.remove(nums[l])
            l += 1

        return complete_subarrays
