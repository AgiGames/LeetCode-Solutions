from collections import Counter
import math

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        num_good_integers = 0
        visited = set()
        def generate_palindromes(palindrome_digits: list[int], left: int, right: int):
            nonlocal num_good_integers

            if left > right:
                palindrome = int("".join(map(str, palindrome_digits)))
                if palindrome % k == 0:
                    frequency_map = Counter(palindrome_digits)
                    hashable = tuple(sorted(frequency_map.items()))
                    if hashable not in visited:
                        visited.add(hashable)
                        total_arrangements = math.factorial(sum(frequency_map.values()))
                        total_arrangements_without_repetition = total_arrangements
                        for num in frequency_map.values():
                            total_arrangements_without_repetition //= math.factorial(num)

                        total_arrangements_with_leading_zeros = 0
                        if frequency_map.get(0, 0) != 0:
                            frequency_map[0] -= 1
                            total_arrangements_with_leading_zeros = math.factorial(sum(frequency_map.values()))
                            for num in frequency_map.values():
                                total_arrangements_with_leading_zeros //= math.factorial(num)

                        num_good_integers += total_arrangements_without_repetition - total_arrangements_with_leading_zeros

            else:
                start = 1 if left == 0 else 0
                for i in range(start, 10):
                    palindrome_digits[left] = palindrome_digits[right] = i
                    generate_palindromes(palindrome_digits, left + 1, right - 1)
        
        ls = [0] * n
        generate_palindromes(ls, 0, n - 1)
        return num_good_integers
