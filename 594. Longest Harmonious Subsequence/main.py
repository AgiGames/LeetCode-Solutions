class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        frequency = dict(Counter(nums))
        
        max_len = 0
        for key in frequency:
            if key + 1 in frequency:
                max_len = max(max_len, frequency[key] + frequency[key + 1])
        
        return max_len
