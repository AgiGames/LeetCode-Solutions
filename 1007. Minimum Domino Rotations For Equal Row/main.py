from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        tops_count = defaultdict(int)
        n = len(tops)

        for top in tops:
            tops_count[top] += 1
            if tops_count[top] == n:
                return 0

        bottoms_count = defaultdict(int)
        possible_nums = set()

        for bottom in bottoms:
            bottoms_count[bottom] += 1
            if bottoms_count[bottom] == n:
                return 0
            if bottoms_count[bottom] + tops_count[bottom] >= n:
                possible_nums.add(bottom)

        min_swaps = float('inf')
        for num in possible_nums:
            can_be_used_for_swapping = True
            for i in range(n):
                if tops[i] != num and bottoms[i] != num:
                    can_be_used_for_swapping = False
                    break
            if can_be_used_for_swapping:
                swaps = 0
                if tops_count[num] < bottoms_count[num]:
                    swaps = min(tops_count[num], n - bottoms_count[num])
                else:
                    swaps = min(bottoms_count[num], n - tops_count[num])
                min_swaps = min(swaps, min_swaps)

        if min_swaps == float('inf'):
            return -1

        return min_swaps
