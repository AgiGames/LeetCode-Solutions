class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adjacency_matrix = defaultdict(list)

        for u, v in edges:
            adjacency_matrix[u].append(v)

        n = len(colors)

        # dp[i][j] -> maximum count of colour j appearing in any path starting from node i
        dp = [[0]*26 for _ in range(n)]

        # 0 -> not visited
        # 1 -> visiting (i.e., dp[current_node] has not been updated yet)
        # 2 -> visited (dp[current_node] has been updated)
        visited_states = [0] * n

        def dfs(current_node):
            
            # if we visit the current_node again even though dp[current_node] was not updated
            if visited_states[current_node] == 1:
                return -1

            # if we visit the current_node again, but dp[current_node] was already updated
            if visited_states[current_node] == 2:
                return dp[current_node][ord(colors[current_node]) - ord('a')]
            
            # we have not yet updated dp[current_node], so set visited_states = 1
            visited_states[current_node] = 1

            # since dfs' results travels from leaves to root, we expect dp[next_node] to have already been updated
            for next_node in adjacency_matrix[current_node]:
                return_result = dfs(next_node) # get the result of next_node

                if return_result == -1: # if it results in a cycle
                    return -1

                # update dp[current_node][colour] for each colour
                for colour in range(26):
                    '''
                    the maximum number of times color 'a' appears on any path starting at node i is equal to the maximum of:
                    the best any of its children can achieve for color 'a'
                    similarly for all colours
                    '''
                    dp[current_node][colour] = max(dp[current_node][colour], dp[next_node][colour])
            
            # we have to add one to the number of occurences of the current colour of the current node
            # as we have not yet considered the colour of the current node
            # and the node itself contributes 1 time to the number of occurences
            colour_coded_column = ord(colors[current_node]) - ord('a')
            dp[current_node][colour_coded_column] += 1
            
            # dp[current_node] has been updated fully, so set visited_states[current_node] = 2
            visited_states[current_node] = 2

            # return the maximum number of times the current node's colour appears in any path starting with current_node
            return dp[current_node][colour_coded_column]

        # for each node, find the maximum frequency of its own color along any path starting from that node.
        answer = 0
        for node in range(n):
            returned_result = dfs(node)
            if returned_result == -1:
                return -1
            answer = max(answer, returned_result)
        
        return answer
