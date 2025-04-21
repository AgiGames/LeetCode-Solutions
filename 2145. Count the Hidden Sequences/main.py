class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        num_differences = len(differences)
        hidden = [0] * (num_differences + 1)

        possible_hidden_sequences = 0

        hidden[0] = lower
        i = 0
        while i < num_differences:
            hidden_at_i_plus_1 = differences[i] + hidden[i]
            hidden[i+1] = hidden_at_i_plus_1
            i += 1

        hidden_range = max(hidden) - min(hidden)
        return max(0, (upper - lower + 1) - hidden_range)
