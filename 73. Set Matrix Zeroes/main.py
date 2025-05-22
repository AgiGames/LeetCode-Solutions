class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])

        changed =[[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 and changed[i][j] == False:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            changed[i][k] = True
                        matrix[i][k] = 0
                    for k in range(n):
                        if matrix[k][j] != 0:
                            changed[k][j] = True
                        matrix[k][j] = 0

        print(matrix)
