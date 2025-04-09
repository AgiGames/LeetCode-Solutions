class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        
        sett = set(nums)
        
        minn = min(nums)

        if minn < k:
            return -1

        if k in sett:
            sett.remove(k)
            
        return len(sett)
