class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0

        hashset = set()
        maxLen = 1
        currLen = 1
        left = 0
        right = 1
        hashset.add(s[left])
        while right < len(s):
            if s[right] in hashset:
                left = left + 1
                hashset.clear()
                hashset.add(s[left])
                right = left + 1
                if currLen > maxLen:
                    maxLen = currLen
                currLen = 1
            else:
                hashset.add(s[right])
                currLen = currLen + 1
                right = right + 1

        if(currLen > maxLen):
            maxLen = currLen

        return maxLen
