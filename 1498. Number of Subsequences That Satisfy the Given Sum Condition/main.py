class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        mod = 10**9 + 7
        n = len(nums)
        nums.sort()
        pow2mod = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2mod[i] = (pow2mod[i - 1] << 1) % mod
        
        l = 0
        r = n - 1
        sub_sequences = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                sub_sequences = (sub_sequences + pow2mod[r-l]) % mod
                l += 1
            else:
                r -= 1
        
        return sub_sequences
