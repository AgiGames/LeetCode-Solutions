class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        num_ways = 0
        
        '''
        // we fix i for child 1 and then see the remaining candies, i.e.
        // remaining = n - i
        // let remaining be = S
        // then, for the remaining two children, let j and k represent the number of candies they get
        // then, j + k = S
        // we can say, 0 <= j <= limit, and 0 <= k <= limit.
        // since k = S - j
        // we can say, 0 <= j <= limit, and 0 <= S - j <= limit
        //                 eq 1                 eq 2
        // split eq 2 into 2 inequalities:
        //  0 <= S - j and S - j <= limit
        //  -> j <= S and S - limit <= j
        //  -> S - limit <= j <= S is equivalent to eq2
        // so for j to satisfy both equations, max(0, S - limit) <= j <= min(limit, S)
        // wkt number of integers between a and b, where b >= a, is b - a + 1
        // then number of possible j between min(limit, S) and max(0, S - limit) is min(limit, S) - max(0, S - limit) + 1
        // so that tells number of possible ways candies can be distributed for a fixed i
        // we add all results over all possible i
        '''

        for i in range(0, min(limit, n) + 1):
            # since we should not have candies remaining after giving i candies to the first child, we check if
            # the candies remaining (S = j + k) is <= limit + limit as j and k can atmost be = limit
            S = n - i
            if S <= limit * 2:
                num_ways += min(limit, S) - max(0, S - limit) + 1
        
        return num_ways
