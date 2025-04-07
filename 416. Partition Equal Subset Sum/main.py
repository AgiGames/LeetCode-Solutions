class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # gets the total sum of the array
        total_sum = sum(nums)
        
        # if total sum is not divisible by 2, then we cannot partition it into two arrays' sums
        if total_sum % 2 != 0:
            return False
        
        # a subset must have its sum to be this target to return true. because if 1 subset sum is total_sum / 2
        # then the other subset must also have sum to be total_sum / 2
        target = total_sum // 2
        
        # stores all sums possible at a certain point
        # stores 0 initially as 0 sum is possible with an empty set
        dp = set([0])

        # iterate through nums
        for num in nums:
            dp_next = set(dp) # in order to not change size of dp set, we make a copy
            for partial_sum in dp: # iterate through each sum we have made so far
                if partial_sum + num == target: # if we include num, and it turns out to add with some other sum
                                                # to return target, we return true
                    return True
                dp_next.add(partial_sum + num) # else, we just add the inclusion result
                                               # (exclusion result already exists in dp set)
            dp = dp_next # new set is now the dp set

        return target in dp # if target exists in dp then it returns true else false
