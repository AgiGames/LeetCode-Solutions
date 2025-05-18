from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        frequencies = dict(Counter(nums))
        
        i = 0
        if 0 in frequencies:
            while frequencies[0] != 0:
                nums[i] = 0
                frequencies[0] -= 1
                i += 1
       
        if 1 in frequencies:
            while frequencies[1] != 0:
                nums[i] = 1
                frequencies[1] -= 1
                i += 1

        if 2 in frequencies:
            while frequencies[2] != 0:
                nums[i] = 2
                frequencies[2] -= 1
                i += 1
