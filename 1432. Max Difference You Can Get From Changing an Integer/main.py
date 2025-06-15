class Solution:
    def maxDiff(self, num: int) -> int:
        
        num_str = str(num)
        n = len(num_str)

        first_non_nine_index = -1        
        for i in range(n):
            if num_str[i] != "9":
                first_non_nine_index = i
                break
        
        first_non_one_index = -1
        for i in range(n):
            if num_str[i] != "1" and num_str[i] != "0":
                first_non_one_index = i
                break

        a_str = ""
        b_str = ""
        if first_non_nine_index != -1:
            a_str = num_str.replace(num_str[first_non_nine_index], "9")
        else:
            a_str = num_str
        
        if first_non_one_index != -1:
            if first_non_one_index == 0:
                b_str = num_str.replace(num_str[first_non_one_index], "1")
            else:
                b_str = num_str.replace(num_str[first_non_one_index], "0")
        else:
            b_str = num_str

        print(a_str, b_str)

        return int(a_str) - int(b_str)
