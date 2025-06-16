class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        minimum = nums[0]
        maximum_difference = -1
        for i in range(1, n):
            if minimum >= nums[i]:
                minimum = nums[i]
            else:
                maximum_difference = max(maximum_difference, nums[i] - minimum)
        
        return maximum_difference
