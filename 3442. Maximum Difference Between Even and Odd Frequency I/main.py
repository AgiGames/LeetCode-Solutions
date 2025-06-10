from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        
        freqs = Counter(list(s))
        
        max_odd_freq = float('inf') * -1
        min_even_freq = float('inf')
    
        for char in freqs:
            freq = freqs[char]

            if freq % 2 == 0:
                min_even_freq = min(min_even_freq, freq)

            else:
                max_odd_freq = max(max_odd_freq, freq)

        return max_odd_freq - min_even_freq
