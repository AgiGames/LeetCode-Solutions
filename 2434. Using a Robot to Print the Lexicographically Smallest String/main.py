from collections import deque

class Solution:
    def robotWithString(self, s: str) -> str:
        
        t = []
        p = []
        n = len(s)

        min_suffix = [None] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        for i in range(n):
            t.append(s[i])
            while t and ((i == n - 1) or (t[-1] <= min_suffix[i + 1])):
                p.append(t.pop())
        
        return ''.join(p)
