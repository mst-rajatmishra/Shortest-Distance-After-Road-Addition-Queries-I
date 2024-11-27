from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the adjacency list for the cities
        adj = {i: [] for i in range(n)}
        
        # The initially existing roads from city i to city i+1 (for i in [0, n-2])
        for i in range(n - 1):
            adj[i].append(i + 1)
        
        def bfs():
            # Perform a BFS from city 0 to city n-1 to find the shortest path
            queue = deque([0])  # Start BFS from city 0
            dist = [-1] * n  # Initialize distances as -1 (meaning unvisited)
            dist[0] = 0  # Distance to itself is 0
            
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if dist[neighbor] == -1:  # If neighbor has not been visited
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
            
            # The distance to city n-1 is the answer
            return dist[n - 1]
        
        result = []
        
        # Process each query
        for u, v in queries:
            # Add the road u -> v
            adj[u].append(v)
            # After adding the new road, find the shortest path from 0 to n-1
            result.append(bfs())
        
        return result
