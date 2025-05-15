class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(groups)
        result = [words[0]]

        for i in range(1, n):
            if groups[i] != groups[i - 1]:
                result.append(words[i])

        return result
