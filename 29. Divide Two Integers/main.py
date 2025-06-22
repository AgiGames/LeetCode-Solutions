class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        a = abs(dividend)
        b = abs(divisor)

        result = 0

        while a >= b:

            multiplier = 1
            largest_number_on_ith_iteration = b

            while a >= (largest_number_on_ith_iteration << 1):
                largest_number_on_ith_iteration <<= 1
                multiplier <<= 1
            
            a -= largest_number_on_ith_iteration
            result += multiplier
        
        if (dividend > 0) != (divisor > 0):
            result = -result
        
        return result
