class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1)//2
            used_pills = 0
            avail = workers[-mid:]            
            can_assign = True

            for task in reversed(tasks[:mid]):
                if avail[-1] >= task:
                    avail.pop()
                else:
                    idx = bisect.bisect_left(avail, task - strength)
                    if idx == len(avail) or used_pills == pills:
                        can_assign = False
                        break
                    used_pills += 1
                    avail.pop(idx)

            if can_assign:
                left = mid
            else:
                right = mid - 1

        return left
