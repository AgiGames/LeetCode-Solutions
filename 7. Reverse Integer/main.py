class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x < 10 and x > -10):
            return x

        sign = 0
        if(x < 0):
            sign = 1

        lower_range = pow(2, 31) * -1
        upper_range = pow(2, 31) - 1

        x = abs(x)
        print(x)
        num_digits = int(math.floor((math.log10(x)) + 1))
        print(num_digits)

        num = 0

        for i in range(num_digits):
            last_digit = x % 10
            x = x // 10
            num = num * 10 + last_digit
            if(num < lower_range or num > upper_range):
                return 0
        
        if(sign):
            return sign * -1 * num
        return num
