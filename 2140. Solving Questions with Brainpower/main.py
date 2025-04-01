class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
        max_points = 0

        cache = {}

        def dfs(question_idx):
            if question_idx >= len(questions):
                return 0

            points = questions[question_idx][0]
            brain_power = questions[question_idx][1]

            if question_idx in cache:
                return cache[question_idx]

            res1 = points + dfs(question_idx + brain_power + 1)
            res2 = dfs(question_idx + 1)

            cache[question_idx] = max(res1, res2)
            return cache[question_idx]

        max_points = dfs(0)
        return max_points
