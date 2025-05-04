from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        domino_frequencies = defaultdict(int)
        n = len(dominoes)

        for domino in dominoes:
            domino_frequencies[(domino[0], domino[1])] += 1

        result = 0
        for domino in dominoes:
            domino_frequencies[(domino[0], domino[1])] -= 1

            a = domino[0]
            b = domino[1]

            if domino_frequencies[(a, b)] > 0:
                result += domino_frequencies[(a, b)]

            if domino_frequencies[(b, a)] > 0 and a != b:
                result += domino_frequencies[(b, a)]

        return result
