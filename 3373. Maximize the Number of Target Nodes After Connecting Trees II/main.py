from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        n = len(edges1) + 1
        m = len(edges2) + 1

        adjacency_matrix1 = defaultdict(list)
        
        for u1, v1 in edges1:
            adjacency_matrix1[u1].append(v1)
            adjacency_matrix1[v1].append(u1)
        
        adjacency_matrix2 = defaultdict(list)

        for u2, v2 in edges2:
            adjacency_matrix2[u2].append(v2)
            adjacency_matrix2[v2].append(u2)

        maximum_possible_node_visits = [0] * n
        
        even_set = [0] * n
        even = [0] * n

        odd_set = [0] * m
        odd = [0] * m

        # i, depth
        def bfs(start, adjacency_matrix, count_even):

            visited = set()
            bfs_queue = deque()
            bfs_queue.append((start, 0))

            while bfs_queue:
                node, depth = bfs_queue.popleft()
                if count_even and depth % 2 == 0:
                    even_set[node] = 1
                elif not count_even and depth % 2 != 0:
                    odd_set[node] = 1
                visited.add(node)
                connections = adjacency_matrix[node]
                for connection in connections:
                    if connection not in visited:
                        visited.add(connection)
                        next_node_state = (connection, depth + 1)
                        bfs_queue.append(next_node_state)

        bfs(0, adjacency_matrix1, True)
        
        bfs(0, adjacency_matrix2, False)
        
        even_set_sum = sum(even_set)
        odd_set_sum = sum(odd_set)

        for i in range(n):
            if even_set[i] == 1:
                even[i] = even_set_sum
            else:
                even[i] = n - even_set_sum
        
        for i in range(m):
            if odd_set[i] == 1:
                odd[i] = m - odd_set_sum
            else:
                odd[i] = odd_set_sum
        
        max_odd = max(odd)

        for i in range(n):
            maximum_possible_node_visits[i] = even[i] + max_odd

        return maximum_possible_node_visits
