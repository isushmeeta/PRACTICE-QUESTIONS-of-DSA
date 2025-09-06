import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency: for each u->v (w) add:
        #   forward edge u->v (w)
        #   reversal edge v->u (2*w)  (available when you're at v)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))     # original forward edge
            adj[v].append((u, 2*w))   # reversed incoming edge (v -> u) at cost 2*w

        INF = 10**30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return -1 if dist[n-1] == INF else dist[n-1]
