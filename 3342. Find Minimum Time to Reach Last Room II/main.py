import heapq
from typing import List, Tuple, Set

class Solution:
    def minTimeToReach(self, t: List[List[int]]) -> int:
        n, m = len(t), len(t[0])

        heap = []

        heapq.heappush(heap, (0, 0, 0, 0))

        visited: Set[Tuple[int, int, int]] = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            cost, i, j, parity = heapq.heappop(heap)

            if (i, j, parity) in visited:
                continue
            visited.add((i, j, parity))

            if i == n - 1 and j == m - 1:
                return cost

            if parity == 0:
                move_cost = 1
                next_parity = 1
            else:
                move_cost = 2
                next_parity = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    wait_time = max(0, t[ni][nj] - cost)
                    total_cost = cost + move_cost + wait_time
                    heapq.heappush(heap, (total_cost, ni, nj, next_parity))

        return -1
