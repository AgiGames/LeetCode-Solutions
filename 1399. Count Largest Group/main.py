from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        cache = defaultdict(int)

        def get_sum_of_digits(num: int) -> int:
            summ = 0
            while(num != 0):
                summ += num % 10
                num //= 10
            return summ

        max_count_with_sum = float('-inf')
        for i in range(1, n + 1):
            summ = get_sum_of_digits(i)
            cache[summ] += 1
            max_count_with_sum = max(cache[summ], max_count_with_sum)

        largest_group_count = 0
        for value in cache.values():
            if (value == max_count_with_sum):
                largest_group_count += 1

        return largest_group_count
