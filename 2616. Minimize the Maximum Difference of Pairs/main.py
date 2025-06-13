class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)
        low = 0
        high = nums[n - 1] - nums[0]

        while low < high:
            mid = low + (high - low) // 2
            pairs = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    pairs += 1
                    i += 1
                i += 1
            if pairs < p:
                low = mid + 1
            else:
                high = mid

        return low
