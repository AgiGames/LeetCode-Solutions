class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        '''
        we first sort the numbers. this is to take advantage of the fact that:
        if a < b and b < c, and if a divides b and b divides c, we can say a divides c.
        the intutition is that a pair of apples can divide a group of 4 apples into two pairs.
        a group of 16 apples can be divided into 4 groups of 4 apples, which in turn can be divided into
        8 pairs of apples.
        '''
        nums.sort()

        # consider n to be the length of the array
        n = len(nums)

        # create a dp array
        dp = [1] * n

        '''
        for the given problem [3, 4, 8, 16] the dp array will look as such:
            nums: 3 4 8 16
            dp:   1 1 1 1

            each number represents "what is the length of a subset, with dp[i] being the last element of the subset".
            this is being initialized to 1, at the start, each number creates a subset of itself, as each number can divide
            itself.
        '''

        # create an array that stores the index of the previous element of the subset ending with element dp[i]
        previous_element_indeces = [-1] * n

        '''
        the previous element indeces array, stores the index of the previous element of the subset ending with element dp[i]
        let us say dp[i] = 16, and we see iteratively if 16 is divisible by the previous numbers [3, 4, 8]
        since 16 is not divisible by 3, we skip that
        we get to the point where 16 is divisible by 4. so we extend the subset to [4, 16] and previous element of 16 is 4.
        so previous_element_indeces[i] = index of 4, which in this context is j
        '''

        # stores the index i, where dp[i] is maximum, which means maximum_subset_length_idx stores the index of the number
        # which is the last element of the largest possible subset
        maximum_subset_length_idx = 0

        # we iterate through each number, checking if previous numbers are divisible with the ith number
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:

                    # if it is divisble, then we must include nums[j] with nums[i]. however, before we do so
                    # we check if we have already included some other number with nums[i], such that the length of the subset
                    # ending at nums[i] is less than if we were to include nums[j] with nums[i]

                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1

                        # since we have now included the number nums[j], we set the previous number's index of nums[i]
                        # to be j

                        previous_element_indeces[i] = j

            # so after finally finding the maximum dp[i] possible for the ith iteration, we must check if
            # dp[i] > dp[maximum_subset_length_idx]. if so, we set maximum_subset_length_idx to i
            if dp[i] > dp[maximum_subset_length_idx]:
                maximum_subset_length_idx = i

        # after we find maximum_subset_length_idx, we build the subset
        result = [] # will hold our result subset

        # we now backtrack from the index of the ending element (maximum_subset_length_idx) to the start, using the
        # previous_element_indeces array
        k = maximum_subset_length_idx
        while k >= 0:
            result.append(nums[k])
            k = previous_element_indeces[k]

        # return our result
        return result
