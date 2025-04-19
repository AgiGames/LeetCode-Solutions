class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def binary_search(l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return r

        nums.sort()
        num_fair_pairs = 0
        n = len(nums)
        for i in range(n):
            low = lower - nums[i]
            up = upper - nums[i]

            num_fair_pairs += binary_search(i + 1, n - 1, up + 1) - binary_search(i + 1, n - 1, low)

        return num_fair_pairs
