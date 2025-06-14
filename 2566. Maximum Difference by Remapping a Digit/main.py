class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        num_str = str(num)
        n = len(num_str)

        non_nine_index = -1
        non_zero_index = -1
        for i in range(n):
            if non_nine_index == -1 and num_str[i] != '9':
                non_nine_index = i
            if non_zero_index == -1 and num_str[i] != '0':
                non_zero_index = i

        maximum_num_str = num_str.replace(num_str[non_nine_index], "9")
        minimum_num_str = num_str.replace(num_str[non_zero_index], "0")

        print(maximum_num_str)
        return int(maximum_num_str) - int(minimum_num_str)
