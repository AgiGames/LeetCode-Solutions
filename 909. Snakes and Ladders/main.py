class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        board = board[::-1]

        def convert_square_to_coordinates(square: int):
            row = (square - 1) // n
            col = (square - 1) % n

            if row % 2 == 1:
                col = (n - 1) - col  # reverse direction on odd rows

            return row, col

        # bfs to find the lowest number of moves required to reach square 36
        # current_square, moves_done
        def bfs():

            visited = set()
            bfs_queue = deque()
            starting_state = (1, 0)
            bfs_queue.append(starting_state)
            
            while bfs_queue:
                current_square, moves_done = bfs_queue.popleft()

                if current_square not in visited:
                    if current_square == n * n:
                        return moves_done

                    x, y = convert_square_to_coordinates(current_square)
                    # print(current_square, x, y)
                    visited.add(current_square)
                    
                    # all possible states are in range current_square + 1 -> current_square + 6 inclusive
                    for i in range(1, 7):
                        next_square = current_square + i
                        if next_square <= n * n:
                            next_x, next_y = convert_square_to_coordinates(next_square)
                            # print(next_square, next_x, next_y)
                            if board[next_x][next_y] != -1:
                                next_square = board[next_x][next_y]
                            next_state = (next_square, moves_done + 1)
                            bfs_queue.append(next_state)

            return -1
        
        return bfs()
