class Solution:
    def countAndSay(self, n: int) -> str:
        
        def run_length_encode(s):
            
            encoded = ""
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    encoded += str(count)
                    encoded += s[i - 1]
                    count = 1

            encoded += str(count)
            encoded += s[-1]

            return encoded

        result = ""
        for i in range(1, n + 1):
            if i == 1:
                result = "1"
            else:
                result = run_length_encode(result)

        return result
