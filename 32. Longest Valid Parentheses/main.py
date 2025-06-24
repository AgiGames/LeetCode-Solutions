class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        n = len(s)
        stack = [-1]
        max_len = 0

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
