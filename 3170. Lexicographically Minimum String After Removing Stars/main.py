class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        deleted = set()
        for i, c in enumerate(s):
            if c == '*':
                character, neg_indx = heapq.heappop(heap)
                deleted.add(-neg_indx)
                deleted.add(i)
            else:
                heapq.heappush(heap, (c, -i))
        
        lexographically_smallest = []
        for i, c in enumerate(s):
            if i in deleted: continue
            lexographically_smallest.append(s[i])

        return ''.join(lexographically_smallest)
