class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(status)

        num_candies = 0

        bfs_queue = deque()
        for box in initialBoxes:
            bfs_queue.append(box)

        found_openable = True
        visited = [False] * n

        while bfs_queue:

            ith_box_id = bfs_queue.popleft()

            if visited[ith_box_id]:
                if status[ith_box_id]:
                    num_candies += candies[ith_box_id]
                    new_boxes = containedBoxes[ith_box_id]
                    for box in new_boxes:
                        bfs_queue.append(box)
                    newly_openable_boxes = keys[ith_box_id]
                    for box in newly_openable_boxes:
                        status[box] = 1
                else:
                    break

            else:
                if status[ith_box_id]:
                    num_candies += candies[ith_box_id]
                    new_boxes = containedBoxes[ith_box_id]
                    for box in new_boxes:
                        bfs_queue.append(box)
                    newly_openable_boxes = keys[ith_box_id]
                    for box in newly_openable_boxes:
                        status[box] = 1
                else:
                    bfs_queue.append(ith_box_id)

            visited[ith_box_id] = True

        return num_candies
