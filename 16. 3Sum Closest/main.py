class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []
        
        min_gap = 10**9
        min_sum = 10**9

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < min_gap:
                    min_gap = abs(target - total)
                    min_sum = total

                if total < target:
                    j += 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j += 1
                else:
                    k -= 1
                    while (j < k and nums[k] == nums[k + 1]):
                        k -= 1

        return min_sum
