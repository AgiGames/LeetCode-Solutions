class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        num_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    num_pairs += 1

        return num_pairs
