class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        s = list(s)
        n = len(s)

        while n % k != 0:
            s.append(fill)
            n += 1
        
        result = []
        for i in range(0, n, k):
            sub_str = ''.join(s[i: i+k])
            result.append(sub_str)

        return result
