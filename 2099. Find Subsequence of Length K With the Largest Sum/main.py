class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        nums_with_indeces = [(num, i) for i, num in enumerate(nums)]

        nums_with_indeces.sort(key=lambda x: -x[0])

        topk = sorted(nums_with_indeces[:k], key=lambda x: x[1])

        result = []
        for (num, i) in topk:
            result.append(num)
        
        return result
