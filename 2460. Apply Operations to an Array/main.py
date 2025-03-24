class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for _ in range(len(nums) - 1):
            if(nums[_] == nums[_ + 1]):
                nums[_] = nums[_] * 2
                nums[_ + 1] = 0

        left = 0 
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums
