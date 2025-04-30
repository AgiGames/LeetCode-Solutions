class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        # floor(log10(num)) -> 1

        result = 0
        for num in nums:
            if (floor(log10(num)) + 1) % 2 == 0:
                result += 1

        return result
