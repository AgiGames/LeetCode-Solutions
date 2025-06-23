import math

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def create_base_10_palindrome(n, is_odd):
            s = str(n)
            half = s[:-1] if is_odd else s
            return int(s + half[::-1])
        
        def to_base_k(input):
            if input == 0:
                return '0'
            digits = []
            while input:
                digits.append(str(input % k))
                input //= k
            return ''.join(reversed(digits))
        
        def num_digits(num):
            return math.floor(math.log10(num)) + 1
            
        sum = 0
        count = 0
        is_odd = True

        i = 1
        while count < n:
            if i != 1 and num_digits(i - 1) < num_digits(i) and is_odd == True:
                i = i - (9 * 10**(num_digits(i) - 2))
                is_odd = False
            
            elif i != 1 and num_digits(i - 1) < num_digits(i) and is_odd == False:
                is_odd = True

            result = create_base_10_palindrome(i, is_odd=is_odd)
            base_k_result = to_base_k(result)
            if base_k_result == base_k_result[::-1]:
                sum += result
                count += 1
            i += 1
        
        return sum
