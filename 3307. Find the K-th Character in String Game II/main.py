class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        total_shifts = 0

        lengths_before_ith_operation = [1]
        for operation in operations:
            lengths_before_ith_operation.append(lengths_before_ith_operation[-1] * 2)
        
        current_char = 'a'
        num_operations = len(operations)

        for i in reversed(range(num_operations)):
            length_before_ith_operation = lengths_before_ith_operation[i]
            operation = operations[i]

            if k <= length_before_ith_operation:
                continue
            
            else:
                k -= length_before_ith_operation

                if operation == 0:
                    continue
                
                else:
                    total_shifts += 1

        return chr(total_shifts % 26 + ord('a'))
