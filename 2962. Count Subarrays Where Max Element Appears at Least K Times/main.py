class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        max_element = max(nums)
        num_max_element_seen = 0
        result = 0

        right = 0
        for left in range(n):
            
            while right < n and num_max_element_seen < k:
                if nums[right] == max_element:
                    num_max_element_seen += 1
                right += 1

            if num_max_element_seen == k:
                result += n - (right - 1)
            
            if nums[left] == max_element:
                num_max_element_seen -= 1

        return result
