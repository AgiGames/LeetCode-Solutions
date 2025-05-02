class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dominoes = list('L' + dominoes + 'R')
        n = len(dominoes)

        previous_force_idx = 0

        for i in range(n):

            if dominoes[i] == '.':
                continue
            
            current_force = dominoes[i]
            previous_force = dominoes[previous_force_idx]

            if current_force == 'R' and dominoes[previous_force_idx] == 'L':
                previous_force_idx = i
                continue

            gap = i - previous_force_idx - 1

            if current_force == 'L' and previous_force == 'R':
                half = gap // 2
                dominoes[previous_force_idx + 1 : previous_force_idx + 1 + half] = ['R'] * half
                dominoes[i - half : i] = ['L'] * half

            if current_force == previous_force:
                if gap > 0:
                    dominoes[previous_force_idx + 1:i] = [current_force] * gap
            
            previous_force_idx = i

        return ''.join(dominoes[1:-1])
