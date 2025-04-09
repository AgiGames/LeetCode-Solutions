class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        num_operations = 0
        start = 0

        while start < l:
            if len(set(nums[start:])) == len(nums[start:]):
                return num_operations

            start += 3

            num_operations += 1

        return num_operations
