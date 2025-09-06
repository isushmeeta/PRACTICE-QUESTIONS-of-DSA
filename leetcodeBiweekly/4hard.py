


from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dp[t][i][j] = min cost to reach (i,j) using t teleports
        dp = [[[INF]*n for _ in range(m)] for _ in range(k+1)]
        dp[0][0][0] = 0  # start at top-left

        # Layer 0: no teleport, standard DP (down/right moves)
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[0][i][j] = min(dp[0][i][j], dp[0][i-1][j] + grid[i][j])
                if j > 0:
                    dp[0][i][j] = min(dp[0][i][j], dp[0][i][j-1] + grid[i][j])

        # Precompute cells grouped by value
        value_to_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_cells[grid[i][j]].append((i,j))
        sorted_values = sorted(value_to_cells.keys(), reverse=True)  # descending

        # Process teleport layers
        for t in range(1, k+1):
            # Start with previous layer costs
            for i in range(m):
                for j in range(n):
                    dp[t][i][j] = dp[t-1][i][j]

            # Teleport propagation: from higher/equal value to lower cells
            best_cost = INF
            for val in sorted_values:
                for x, y in value_to_cells[val]:
                    best_cost = min(best_cost, dp[t-1][x][y])
                for x, y in value_to_cells[val]:
                    dp[t][x][y] = min(dp[t][x][y], best_cost)

            # Normal moves after teleport
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        dp[t][i][j] = min(dp[t][i][j], dp[t][i-1][j] + grid[i][j])
                    if j > 0:
                        dp[t][i][j] = min(dp[t][i][j], dp[t][i][j-1] + grid[i][j])

        return min(dp[t][m-1][n-1] for t in range(k+1))
