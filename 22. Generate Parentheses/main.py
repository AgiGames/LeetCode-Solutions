class Solution:
    def generateParenthesis(self, n):

        result = []

        def dfs(string, parentheses_opened, parentheses_closed):
            if parentheses_opened == parentheses_closed and parentheses_closed == n:
                return string
            if parentheses_opened < n:
                ith_result = dfs(string + "(", parentheses_opened + 1, parentheses_closed)
                if ith_result is not None:
                    result.append(ith_result)
            if parentheses_closed < parentheses_opened:
                ith_result = dfs(string + ")", parentheses_opened, parentheses_closed + 1)
                if ith_result is not None:
                    result.append(ith_result)

        dfs("", 0, 0)
        return result
