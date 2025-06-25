class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        m = len(nums2)

        left = -10**10
        right = 10**10

        def count_products_less_than_or_equal_to(mid):

            total_products = 0
            for a in nums1:
                if a < 0:
                    # a is less than 0
                    # we have to find, how many numbers, when multiplied with a, gives
                    # a * b <= mid
                    # since a is less than 0 in this case
                    # a * b / a <= mid / a will become b >= mid / a
                    # it's experimentally found that ceil(mid / a) makes it such that the condition remains true, if mid is not divisible by a
                    b = math.ceil(mid / a)
                    total_products += (m - bisect.bisect_left(nums2, b)) # so now we find the first index of b >= mid / a
                    
                elif a == 0:
                    if mid >= 0:
                        total_products += m
                else:
                    # a is greater than 0
                    # we have to find, how many numbers when multiplied with a, gives
                    # a * b <= mid
                    # since a is greater than 0 in this case
                    # a * b / a <= mid / a will become b <= mid / a
                    # it's experimentally found that mid // a makes it such that the condition remains true, if mid is not divisible by a
                    b = mid // a

                    total_products += bisect.bisect_right(nums2, b) # bisect returns the first index that is greater than b for some reason
            
            return total_products

        while left < right:
            mid = left + ((right - left) // 2)
            products = count_products_less_than_or_equal_to(mid)
            if products < k:
                left = mid + 1
            else:
                right = mid

        return left
