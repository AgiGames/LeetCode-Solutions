class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        total_columns_possible = 3**m
        mod = 10**9+7

        dp = [[0] * total_columns_possible for _ in range(n + 1)]
        valid_columns = []
        all_possible_patterns = [[] for _ in range(total_columns_possible)]

        for i in range(total_columns_possible):
            base_3_val = i
            ith_column_is_valid = True
            for _ in range(m):
                all_possible_patterns[i].append(base_3_val % 3)
                base_3_val //= 3
            for j in range(1, m):
                if all_possible_patterns[i][j] == all_possible_patterns[i][j - 1]:
                    ith_column_is_valid = False
                    break
            if ith_column_is_valid:
                valid_columns.append(i)

        columns_are_compatible = [[True] * total_columns_possible for _ in range(total_columns_possible)]
        for i in valid_columns:
            for j in valid_columns:
                for k in range(m):
                    if all_possible_patterns[i][k] == all_possible_patterns[j][k]:
                        columns_are_compatible[i][j] = False
                        break

        for i in valid_columns:
            dp[1][i] = 1
        for column in range(2, n+1):
            for i in valid_columns:
                total_valid_ways_possible = 0
                for j in valid_columns:
                    if columns_are_compatible[i][j]:
                        total_valid_ways_possible += dp[column - 1][j]
                dp[column][i] = total_valid_ways_possible % mod

        return sum(dp[n][i] for i in valid_columns) % mod
