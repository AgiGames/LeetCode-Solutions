from collections import defaultdict

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
        distances_from_node_1 = [-1] * n
        distances_from_node_2 = [-1] * n

        visited = set()
        def dfs(node, distance, distances_from_node):
            if node in visited:
                return
            distances_from_node[node] = distance
            visited.add(node)
            next_node = edges[node]
            if next_node != -1:
                dfs(next_node, distance + 1, distances_from_node)
        
        dfs(node1, 0, distances_from_node_1)

        visited = set()
        dfs(node2, 0, distances_from_node_2)

        previous_minimized_maximum_distance = float('inf')
        previous_minimized_maximum_distance_i = -1
        for i in range(n):
            if distances_from_node_1[i] != -1 and distances_from_node_2[i] != -1:
                maximum_from_node1_and_node2 = max(distances_from_node_1[i], distances_from_node_2[i])
                if maximum_from_node1_and_node2 < previous_minimized_maximum_distance:
                    previous_minimized_maximum_distance = maximum_from_node1_and_node2
                    previous_minimized_maximum_distance_i = i
        
        return previous_minimized_maximum_distance_i
