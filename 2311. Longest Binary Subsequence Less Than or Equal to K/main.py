class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)

        power_value = 1
        result = 0
        length = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                length += 1
            else:
                if result + power_value <= k:
                    result += power_value
                    length += 1

            power_value <<= 1

        return length
