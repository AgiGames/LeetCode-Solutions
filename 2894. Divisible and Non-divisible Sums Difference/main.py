class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        nums1 = [0] * (n + 1)
        nums2 = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % m == 0:
                nums2[i] = i
            if i % m != 0:
                nums1[i] = i
        
        return sum(nums1) - sum(nums2)
