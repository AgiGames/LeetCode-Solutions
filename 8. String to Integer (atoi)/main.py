class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip()

        if(len(s) <= 0):
            return 0

        num = 0
        digits = 0
        
        num_start = 0
        if(s[num_start] != '+' and s[num_start] != '-' and s[num_start] != '0'
                                                         and s[num_start] != '1'
                                                         and s[num_start] != '2'
                                                         and s[num_start] != '3'
                                                         and s[num_start] != '4'
                                                         and s[num_start] != '5'
                                                         and s[num_start] != '6'
                                                         and s[num_start] != '7'
                                                         and s[num_start] != '8'
                                                         and s[num_start] != '9'):
            return 0
        
        sign = 0
        if(s[num_start] == '-'):
            sign = 1
            num_start = num_start + 1
        elif(s[num_start] == '+'):
            num_start = num_start + 1

        i = num_start
        while((i < len(s)) and (s[i] == '0' or
              s[i] == '1' or
              s[i] == '2' or
              s[i] == '3' or
              s[i] == '4' or
              s[i] == '5' or
              s[i] == '6' or
              s[i] == '7' or
              s[i] == '8' or
              s[i] == '9')):
            
            num = num * 10 + (ord(s[i]) - ord('0'))
            i = i + 1
        
        if(sign == 1):
            num = num * -1

        if(num < -2147483648):
            num = -2147483648
        if(num > 2147483647):
            num = 2147483647

        return num
