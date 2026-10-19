class Solution:
    def climbStairs(self, n: int) -> int:
        #base case:
        def dfs(i): #dfs(i) returns the number of way climbing to n at stair i
            if i == n:
                return 1
            if i > n:
                return 0
            return dfs(i+1) + dfs(i+2)
        return dfs(0)


                                                                                                                                                                                                                          
        