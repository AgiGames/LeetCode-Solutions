class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cache = {}

        def dfs(nums, i, xor_result):
            
            if (i, xor_result) in cache:
                return cache[(i, xor_result)]

            if i >= len(nums):
                return xor_result
            
            # first exclude the number
            include = dfs(nums, i + 1, xor_result)

            xor_result = xor_result ^ nums[i]

            # then include the number

            exclude = dfs(nums, i + 1, xor_result)

            cache[(i, xor_result)] = include + exclude

            return include + exclude

        return dfs(nums, 0, 0)
