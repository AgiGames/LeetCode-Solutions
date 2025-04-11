class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        num_symmetric_numbers = 0
        for i in range(low, high + 1):
            i_str = str(i)
            n = len(i_str)
            if n % 2 != 0:
                continue
            else:
                ptr_low = 0
                ptr_high = n - 1
                sum_left = 0
                sum_right = 0
                while ptr_low < ptr_high:
                    sum_left += int(i_str[ptr_low])
                    sum_right += int(i_str[ptr_high])
                    ptr_low += 1
                    ptr_high -= 1
                if sum_left == sum_right:
                    num_symmetric_numbers += 1

        return num_symmetric_numbers
