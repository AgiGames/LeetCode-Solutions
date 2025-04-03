class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        max_pref = [0] * n
        max_pref[0] = nums[0]
        for i in range(1, n):
            max_pref[i] = max(max_pref[i - 1], nums[i])

        max_suff = [0] * n
        max_suff[n - 1] = nums[n - 1]
        for k in range(n - 2, -1, -1):
            max_suff[k] = max(max_suff[k + 1], nums[k])

        max_val = 0
        for j in range(1, n - 1):
            max_val = max(max_val, (max_pref[j - 1] - nums[j]) * max_suff[j + 1])
        
        return max_val
