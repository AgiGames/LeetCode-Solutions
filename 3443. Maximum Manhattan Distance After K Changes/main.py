class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        def get_max_distance(main_direction_one, main_direction_two, s, k):
            
            manhattan_distance = 0
            max_manhattan_distance = 0
            for direction in s:
                if main_direction_one == direction or main_direction_two == direction:
                    manhattan_distance += 1
                else:
                    if k > 0:
                        manhattan_distance += 1
                        k -= 1
                    else:
                        max_manhattan_distance = max(max_manhattan_distance, manhattan_distance)
                        manhattan_distance -= 1
            
            max_manhattan_distance = max(max_manhattan_distance, manhattan_distance)
            return max_manhattan_distance

        if k == len(s): # that means we can change all characters into N thus being k distance away
            return k

        nw = get_max_distance('N', 'W', s, k)
        ne = get_max_distance('N', 'E', s, k)
        sw = get_max_distance('S', 'W', s, k)
        se = get_max_distance('S', 'E', s, k)

        return max(nw, ne, sw, se)
