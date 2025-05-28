from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
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
        
        # i, depth_left
        def depth_limited_bfs(start, adjacency_matrix, starting_depth):
            
            if starting_depth < 0:
                return 0

            visited = set()
            bfs_queue = deque()
            bfs_queue.append((start, starting_depth))
            nodes_visited = 0

            while bfs_queue:
                node, depth_left = bfs_queue.popleft()
                nodes_visited += 1
                visited.add(node)
                if depth_left > 0:
                    connections = adjacency_matrix[node]
                    for connection in connections:
                        if connection not in visited:
                            visited.add(connection)
                            next_node_state = (connection, depth_left - 1)
                            bfs_queue.append(next_node_state)

            return nodes_visited
        
        max_node_visits_from_tree_two = -1 * float('inf')
        for i in range(m):
            max_node_visits_from_tree_two = max(max_node_visits_from_tree_two, depth_limited_bfs(i, adjacency_matrix2, k - 1))
        
        for i in range(n):
            maximum_possible_node_visits[i] = depth_limited_bfs(i, adjacency_matrix1, k) + max_node_visits_from_tree_two
        
        return maximum_possible_node_visits
