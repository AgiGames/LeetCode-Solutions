from collections import deque

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        visited = [False] * len(s)
        queue = deque()
        n = numRows
        output_string = ""
        wave_length = (n - 1) + (n - 2) + 1
        wave_length = max(wave_length, 1)
        j = 0
        while j < len(s):
            queue.append(j)
            visited[j] = True
            j = j + wave_length

        s = s.ljust(j+1)
        queue.append(j)
        visited = visited + [False] * (j - len(visited) + 1)

        while queue:
            ith_element = queue.popleft()
            output_string = output_string + s[ith_element]
            if(ith_element - 1 >= 0):
                if(visited[ith_element - 1] == False):
                    queue.append(ith_element - 1)
                    visited[ith_element - 1] = True
            if(ith_element + 1 < len(s)):
                if(visited[ith_element + 1] == False):
                    queue.append(ith_element + 1)
                    visited[ith_element + 1] = True


        return output_string.replace(" ", "")
