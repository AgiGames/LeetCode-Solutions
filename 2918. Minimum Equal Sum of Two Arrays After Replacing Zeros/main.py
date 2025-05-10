class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)

        nums1_zeroes = 0
        for n in nums1:
            if n == 0:
                nums1_zeroes += 1
        
        nums2_zeroes = 0
        for n in nums2:
            if n == 0:
                nums2_zeroes += 1

        if nums1_zeroes == 0 and nums2_zeroes == 0:
            if nums1_sum == nums2_sum:
                return nums1_sum
            return -1

        minimum_value_nums1_can_reach = nums1_sum + nums1_zeroes
        minimum_value_nums2_can_reach = nums2_sum + nums2_zeroes

        if nums1_zeroes == 0:
            if minimum_value_nums2_can_reach <= nums1_sum:
                return nums1_sum
            return -1
        
        if nums2_zeroes == 0:
            if minimum_value_nums1_can_reach <= nums2_sum:
                return nums2_sum
            return -1

        else:
            return max(minimum_value_nums1_can_reach, minimum_value_nums2_can_reach)
