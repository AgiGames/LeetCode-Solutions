class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        n = len(word)

        if numFriends == 1:
            return word

        starting_word_size = (n - numFriends) + 1

        lexographically_largest = ""
        for i in range(n):
            lexographically_largest = max(lexographically_largest, word[i:i + starting_word_size])
        
        return lexographically_largest
