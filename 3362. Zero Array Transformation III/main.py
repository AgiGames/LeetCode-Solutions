import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        decrements = [0] * (n + 1)

        ends = [[] for _ in range(n)]
        for query in queries:
            ends[query[0]].append(query[1])

        heap = []
        decrement = 0
        for i in range(n):
            key = nums[i]
            decrement += decrements[i]
            for j in ends[i]:
                heapq.heappush(heap, -j)
            
            while key > decrement and len(heap) > 0 and -heap[0] >= i:
                decrements[-heap[0] + 1] -= 1
                heapq.heappop(heap)
                decrement += 1
            if key > decrement:
                return -1
        
        return len(heap)
