class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return []

        number_to_chars = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                           7: "pqrs", 8: "tuv", 9: "wxyz"}

        if len(digits) == 1:
            return list(number_to_chars[int(digits)])

        n = len(digits)
        strings = []

        first_num_idx = 0
        second_num_idx = 1
        first_num = int(digits[first_num_idx])
        second_num = int(digits[second_num_idx])

        second_num_chars = number_to_chars[second_num]
        first_num_chars = number_to_chars[first_num]

        for fnc in first_num_chars:
            for snc in second_num_chars:
                strings.append(fnc + snc)

        nth_num_idx = second_num_idx + 1
        while nth_num_idx < n:
            nth_strings = []
            nth_num = int(digits[nth_num_idx])
            nth_num_chars = number_to_chars[nth_num]
            for string in strings:
                for nnc in nth_num_chars:
                    nth_strings.append(string + nnc)
            strings = nth_strings
            nth_num_idx += 1

        return strings
