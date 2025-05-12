from collections import defaultdict

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        numbers = []
        frequency_map = defaultdict(int)

        for digit in digits:
            frequency_map[digit] += 1

        for i in range(1, 10):
            if frequency_map[i] == 0: continue
            frequency_map[i] -= 1

            for j in range(0, 10):
                if frequency_map[j] == 0: continue
                frequency_map[j] -= 1
                
                for k in range(0, 9, 2):
                    if frequency_map[k] == 0: continue
                    frequency_map[k] -= 1

                    number = i * 100 + j * 10 + k
                    numbers.append(number)
                    frequency_map[k] += 1
                frequency_map[j] += 1
            frequency_map[i] += 1

        return numbers
