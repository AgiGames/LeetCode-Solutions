class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        result = 1
        n = len(word)
        i = 0
        freq = 0
        while i <= n:
            if (i == n):
                result += freq - 1
                freq = 1
                break

            if (i > 0 and word[i] != word[i - 1]):
                result += freq - 1
                freq = 1
            else:
                freq += 1
            i += 1

        return result
