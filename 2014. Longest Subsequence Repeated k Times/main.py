class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        n = len(s)

        frequencies = dict(Counter(s))
        chars = []
        for char in map(chr, range(ord('z'), ord('a') -1, -1)):
            if char in frequencies and frequencies[char] >= k:
                chars.append(char)

        result = ""

        max_len = n // k

        def occursKTimes(subsequence: str, m):
            if m > n // k:
                return False 
            i = 0
            count = 0
            for char in s:
                if i < m and char == subsequence[i]:
                    i += 1
                    if i == m:
                        count += 1
                        i = 0
                        if count == k:
                            return True

            return False

        result = ""
        result_len = 0
        
        def dfs(sub_sequence, m):
            
            nonlocal result
            nonlocal result_len

            if m > 0 and not occursKTimes(sub_sequence, m):
                return
            
            if m > result_len:
                result = sub_sequence
                result_len = m

            for char in chars:
                dfs(sub_sequence + char, m + 1)
        
        dfs("", 0)

        return result
