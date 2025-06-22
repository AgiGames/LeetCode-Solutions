class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        n = len(s)
        substr_len = len(words[0])
        num_words = len(words)
        window_size = num_words * substr_len

        left = 0
        right = window_size - 1

        word_frequencies = dict(Counter(words))
        
        
        def dictionaries_are_equal(static_dict, dynamic_dict):
            
            for key, value in static_dict.items():
                if dynamic_dict[key] != value:
                    return False
            return True

        result = []

        while right < n:
            
            window_word_frequencies = defaultdict(int)

            for i in range(num_words):
                word = s[left+(i*substr_len): left+(i*substr_len+substr_len)]
                window_word_frequencies[word] += 1

            if dictionaries_are_equal(word_frequencies, window_word_frequencies):
                result.append(left)

            word_to_be_removed = s[left: left + substr_len]
            window_word_frequencies[word_to_be_removed] -= 1
            left += 1
            next_word_start = right + 1
            right += 1

            next_word = s[next_word_start: next_word_start + substr_len]
            window_word_frequencies[next_word] += 1
        return result
