class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        indeces = []
        for i in range(len(words)):
            if x in words[i]:
                indeces.append(i)
        
        return indeces
