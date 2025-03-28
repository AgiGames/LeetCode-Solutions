from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = deque()

        matching_brackets = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st or st[-1] != matching_brackets[c]:  
                    return False
                st.pop()
        
        return not st
