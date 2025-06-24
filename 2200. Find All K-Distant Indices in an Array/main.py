class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        key_indexes = []
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                key_indexes.append(i)

        result = []
        for i in range(n):
            for key_index in key_indexes:
                if abs(i - key_index) <= k:
                    result.append(i)
                    break
        
        return result
