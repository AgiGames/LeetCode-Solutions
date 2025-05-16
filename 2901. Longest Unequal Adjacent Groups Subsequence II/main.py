class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        def is_valid(word_one, word_two):
            word_one_len = len(word_one)
            word_two_len = len(word_two)
            if word_one_len != word_two_len:
                return False
            num_chars_different = 0
            for i in range(word_one_len):
                if word_one[i] != word_two[i]:
                    num_chars_different += 1
                    if num_chars_different > 1:
                        return False
            return num_chars_different == 1

        num_words = len(words)
        previous_word_indeces = [-1] * num_words
        dp = [1] * num_words
        index_of_longest_subsequence = 0
        for i in range(num_words):
            for j in range(i):
                if is_valid(words[j], words[i]) and groups[i] != groups[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    previous_word_indeces[i] = j
            if dp[i] > dp[index_of_longest_subsequence]:
                index_of_longest_subsequence = i
        
        # retrace from index of largest subsequence
        result = []
        i = index_of_longest_subsequence
        while i != -1:
            result.append(words[i])
            i = previous_word_indeces[i]

        return result[::-1]
