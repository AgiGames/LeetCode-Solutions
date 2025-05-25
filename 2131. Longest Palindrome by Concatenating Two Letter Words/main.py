from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        word_frequencies = dict(Counter(words))
        palindrome_size = 0
        can_come_into_middle = False

        for word in word_frequencies:
            frequency = word_frequencies[word]
            reversed_word = word[::-1]
            if word == reversed_word:
                palindrome_size += (frequency // 2) * 4
                if frequency % 2 == 1:
                    can_come_into_middle = True

            elif word < reversed_word and reversed_word in word_frequencies:
                palindrome_size += min(frequency, word_frequencies[reversed_word]) * 4
        
        if can_come_into_middle:
            return palindrome_size + 2
        return palindrome_size
