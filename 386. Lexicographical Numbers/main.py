class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        result = []
    
        def dfs(number):
            if number == 0:
                for i in range(1, min(9, n) + 1):
                    next_number = (number * 10) + i
                    # print(next_number)
                    if next_number <= n:
                        result.append(next_number)
                        dfs(next_number)
            else:
                for i in range(min(9, n) + 1):
                    next_number = (number * 10) + i
                    # print(next_number)
                    if next_number <= n:
                        result.append(next_number)
                        dfs(next_number)

        dfs(0)

        return result
