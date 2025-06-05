from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        n = len(s1)

        equivalence = defaultdict(list)

        for i in range(n):
            a = s1[i]
            b = s2[i]

            equivalence[a].append(b)
            equivalence[b].append(a)

        def dfs(character, visited):
            visited.add(character)
            min_character = character
            for next_character in equivalence[character]:
                if next_character not in visited:
                    min_character = min(min_character, dfs(next_character, visited))
            return min_character

        result = []
        for base_character in baseStr:
            visited = set()
            result.append(dfs(base_character, visited))
        
        return ''.join(result)
