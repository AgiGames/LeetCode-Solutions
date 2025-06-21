class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        frequencies = list(Counter(word).values())
        frequencies.sort()

        num_frequencies = len(frequencies)

        min_deleted_chars = float('inf')
        total_frequency_sum = sum(frequencies)
        num_deleted_to_left = 0
        window_sum = 0
        j = 0

        for i in range(num_frequencies):
            fromm = frequencies[i]
            to = fromm + k

            while j < num_frequencies and frequencies[j] <= to:
                window_sum += frequencies[j]
                j += 1

            num_elements_to_right = num_frequencies - j
            right_frequency_sum = total_frequency_sum - window_sum

            num_deleted_to_right = right_frequency_sum - (num_elements_to_right * to)

            total_deletions = num_deleted_to_left + num_deleted_to_right
            min_deleted_chars = min(min_deleted_chars, total_deletions)

            total_frequency_sum -= frequencies[i]
            num_deleted_to_left += frequencies[i]
            window_sum -= frequencies[i]

        return min_deleted_chars
