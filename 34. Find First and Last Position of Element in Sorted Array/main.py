class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        def search(is_searching_left):
            l = 0
            r = n - 1
            idx = -1

            while l <= r:
                mid = l + ((r - l) // 2)
                
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        r = mid - 1
                    else:
                        l = mid + 1
        
            return idx
        
        left = search(True)
        right = search(False)

        return [left, right]
