from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        min_rabbits = 0
        for x, count in Counter(answers).items():
            group_size = x + 1
            num_groups = (count + group_size - 1) // group_size
            min_rabbits += num_groups * group_size
        return min_rabbits
