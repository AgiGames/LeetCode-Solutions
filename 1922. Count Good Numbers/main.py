import math

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        num_even_digits = int(math.ceil(n / 2))
        
        num_prime_digits = int(n - num_even_digits)

        modulo_number = (10**9 + 7)

        def modulo_exponent(base, exp):
            result = 1

            base = base % modulo_number

            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % modulo_number
                base = (base * base) % modulo_number
                exp //= 2

            return result

        return (modulo_exponent(5, num_even_digits) * modulo_exponent(4, num_prime_digits)) % modulo_number
