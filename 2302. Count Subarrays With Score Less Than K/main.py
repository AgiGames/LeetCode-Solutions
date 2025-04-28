class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for idx in range(n):
            prefix_sum[idx + 1] = prefix_sum[idx] + nums[idx]

        result = 0
        j = 0

        for i in range(n):
            while j < n and (prefix_sum[j + 1] - prefix_sum[i]) * (j - i + 1) < k:
                j += 1

            result += (j - i)

        return result
